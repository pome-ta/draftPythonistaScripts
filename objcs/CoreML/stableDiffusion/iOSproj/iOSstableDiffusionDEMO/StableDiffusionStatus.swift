//
//  StableDiffusionStatus.swift
//  iOSstableDiffusionDEMO
//  
//  Created by pome-ta on 2023/01/03
//  
//

import Foundation

enum StableDiffusionStatus {
    case ready
    case loadStart
    case loadFinish
    case generateStart
    case generateFinish
    case error
    
    var message: String {
        switch self {
        case .ready:
            return "準備中"
        case .loadStart:
            return "モデルの読み込みを開始しました"
        case .loadFinish:
            return "モデルの読み込みが終了しました"
        case .generateStart:
            return "画像生成を開始しました"
        case .generateFinish:
            return "画像生成が終了しました"
        case .error:
            return "エラーが発生しました"
        }
    }
}
