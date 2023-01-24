// For licensing see accompanying LICENSE.md file.
// Copyright (C) 2022 Apple Inc. All Rights Reserved.

import CoreML

/// A class to manage and gate access to a Core ML model
// Core ML モデルへのアクセスを管理およびゲートするクラス
///
/// It will automatically load a model into memory when needed or requested
// 必要に応じて、または要求されたときに、モデルをメモリに自動的にロードします
/// It allows one to request to unload the model from memory
// モデルをメモリからアンロードするように要求できます
@available(iOS 16.2, macOS 13.1, *)
public final class ManagedMLModel: ResourceManaging {

    /// The location of the model
    var modelURL: URL

    /// The configuration to be used when the model is loaded
    var configuration: MLModelConfiguration

    /// The loaded model (when loaded)
    // ロードされたモデル (ロードされた場合)
    var loadedModel: MLModel?

    /// Queue to protect access to loaded model
    // ロードされたモデルへのアクセスを保護するためのキュー
    var queue: DispatchQueue

    /// Create a managed model given its location and desired loaded configuration
    // 場所と目的のロード済み構成を指定して、管理対象モデルを作成します
    ///
    /// - Parameters:
    ///     - url: The location of the model
           // url: モデルの場所
    ///     - configuration: The configuration to be used when the model is loaded/used
           // 構成: モデルのロード/使用時に使用される構成
    /// - Returns: A managed model that has not been loaded
    // 戻り値: ロードされていないマネージド モデル
    public init(modelAt url: URL, configuration: MLModelConfiguration) {
        self.modelURL = url
        self.configuration = configuration
        self.loadedModel = nil
        self.queue = DispatchQueue(label: "managed.\(url.lastPathComponent)")
    }

    /// Instantiation and load model into memory
    public func loadResources() throws {
        try queue.sync {
            try loadModel()
        }
    }

    /// Unload the model if it was loaded
    public func unloadResources() {
        queue.sync {
            loadedModel = nil
        }
    }

    /// Perform an operation with the managed model via a supplied closure.
    // 提供されたクロージャーを介してマネージド モデルで操作を実行します。
    ///  The model will be loaded and supplied to the closure and should only be
    ///  used within the closure to ensure all resource management is synchronized
    
    // モデルはクロージャーにロードされて提供され、すべてのリソース管理が確実に同期されるようにクロージャー内でのみ使用する必要があります
    ///
    /// - Parameters:
    ///     - body: Closure which performs and action on a loaded model
            // body: ロードされたモデルに対して実行およびアクションを実行するクロージャ
    /// - Returns: The result of the closure
        // 戻り値: クロージャの結果
    /// - Throws: An error if the model cannot be loaded or if the closure throws
        // スロー: モデルをロードできない場合、またはクロージャーがスローした場合はエラー
    public func perform<R>(_ body: (MLModel) throws -> R) throws -> R {
        return try queue.sync {
            try autoreleasepool {
                try loadModel()
                return try body(loadedModel!)
            }
        }
    }

    private func loadModel() throws {
        if loadedModel == nil {
            loadedModel = try MLModel(contentsOf: modelURL,
                                      configuration: configuration)
        }
    }


}
