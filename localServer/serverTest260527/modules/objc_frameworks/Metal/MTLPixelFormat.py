from enum import IntEnum


class MTLPixelFormat(IntEnum):
  #[doc(alias = "MTLPixelFormatInvalid")]
  invalid = 0
  #[doc(alias = "MTLPixelFormatA8Unorm")]
  a8Unorm = 1
  #[doc(alias = "MTLPixelFormatR8Unorm")]
  r8Unorm = 10
  #[doc(alias = "MTLPixelFormatR8Unorm_sRGB")]
  r8Unorm_sRGB = 11
  #[doc(alias = "MTLPixelFormatR8Snorm")]
  r8Snorm = 12
  #[doc(alias = "MTLPixelFormatR8Uint")]
  r8Uint = 13
  #[doc(alias = "MTLPixelFormatR8Sint")]
  r8Sint = 14
  #[doc(alias = "MTLPixelFormatR16Unorm")]
  r16Unorm = 20
  #[doc(alias = "MTLPixelFormatR16Snorm")]
  r16Snorm = 22
  #[doc(alias = "MTLPixelFormatR16Uint")]
  r16Uint = 23
  #[doc(alias = "MTLPixelFormatR16Sint")]
  r16Sint = 24
  #[doc(alias = "MTLPixelFormatR16Float")]
  r16Float = 25
  #[doc(alias = "MTLPixelFormatRG8Unorm")]
  rg8Unorm = 30
  #[doc(alias = "MTLPixelFormatRG8Unorm_sRGB")]
  rg8Unorm_sRGB = 31
  #[doc(alias = "MTLPixelFormatRG8Snorm")]
  rg8Snorm = 32
  #[doc(alias = "MTLPixelFormatRG8Uint")]
  rg8Uint = 33
  #[doc(alias = "MTLPixelFormatRG8Sint")]
  rg8Sint = 34
  #[doc(alias = "MTLPixelFormatB5G6R5Unorm")]
  b5G6R5Unorm = 40
  #[doc(alias = "MTLPixelFormatA1BGR5Unorm")]
  a1BGR5Unorm = 41
  #[doc(alias = "MTLPixelFormatABGR4Unorm")]
  abgr4Unorm = 42
  #[doc(alias = "MTLPixelFormatBGR5A1Unorm")]
  bgr5A1Unorm = 43
  #[doc(alias = "MTLPixelFormatR32Uint")]
  r32Uint = 53
  #[doc(alias = "MTLPixelFormatR32Sint")]
  r32Sint = 54
  #[doc(alias = "MTLPixelFormatR32Float")]
  r32Float = 55
  #[doc(alias = "MTLPixelFormatRG16Unorm")]
  rg16Unorm = 60
  #[doc(alias = "MTLPixelFormatRG16Snorm")]
  rg16Snorm = 62
  #[doc(alias = "MTLPixelFormatRG16Uint")]
  rg16Uint = 63
  #[doc(alias = "MTLPixelFormatRG16Sint")]
  rg16Sint = 64
  #[doc(alias = "MTLPixelFormatRG16Float")]
  rg16Float = 65
  #[doc(alias = "MTLPixelFormatRGBA8Unorm")]
  rgba8Unorm = 70
  #[doc(alias = "MTLPixelFormatRGBA8Unorm_sRGB")]
  rgba8Unorm_sRGB = 71
  #[doc(alias = "MTLPixelFormatRGBA8Snorm")]
  rgba8Snorm = 72
  #[doc(alias = "MTLPixelFormatRGBA8Uint")]
  rgba8Uint = 73
  #[doc(alias = "MTLPixelFormatRGBA8Sint")]
  rgba8Sint = 74
  #[doc(alias = "MTLPixelFormatBGRA8Unorm")]
  bgra8Unorm = 80
  #[doc(alias = "MTLPixelFormatBGRA8Unorm_sRGB")]
  bgra8Unorm_sRGB = 81
  #[doc(alias = "MTLPixelFormatRGB10A2Unorm")]
  rgb10A2Unorm = 90
  #[doc(alias = "MTLPixelFormatRGB10A2Uint")]
  rgb10A2Uint = 91
  #[doc(alias = "MTLPixelFormatRG11B10Float")]
  rg11B10Float = 92
  #[doc(alias = "MTLPixelFormatRGB9E5Float")]
  rgb9E5Float = 93
  #[doc(alias = "MTLPixelFormatBGR10A2Unorm")]
  bgr10A2Unorm = 94
  #[doc(alias = "MTLPixelFormatBGR10_XR")]
  bgr10_XR = 554
  #[doc(alias = "MTLPixelFormatBGR10_XR_sRGB")]
  bgr10_XR_sRGB = 555
  #[doc(alias = "MTLPixelFormatRG32Uint")]
  rg32Uint = 103
  #[doc(alias = "MTLPixelFormatRG32Sint")]
  rg32Sint = 104
  #[doc(alias = "MTLPixelFormatRG32Float")]
  rg32Float = 105
  #[doc(alias = "MTLPixelFormatRGBA16Unorm")]
  rgba16Unorm = 110
  #[doc(alias = "MTLPixelFormatRGBA16Snorm")]
  rgba16Snorm = 112
  #[doc(alias = "MTLPixelFormatRGBA16Uint")]
  rgba16Uint = 113
  #[doc(alias = "MTLPixelFormatRGBA16Sint")]
  rgba16Sint = 114
  #[doc(alias = "MTLPixelFormatRGBA16Float")]
  rgba16Float = 115
  #[doc(alias = "MTLPixelFormatBGRA10_XR")]
  bgra10_XR = 552
  #[doc(alias = "MTLPixelFormatBGRA10_XR_sRGB")]
  bgra10_XR_sRGB = 553
  #[doc(alias = "MTLPixelFormatRGBA32Uint")]
  rgba32Uint = 123
  #[doc(alias = "MTLPixelFormatRGBA32Sint")]
  rgba32Sint = 124
  #[doc(alias = "MTLPixelFormatRGBA32Float")]
  rgba32Float = 125
  #[doc(alias = "MTLPixelFormatBC1_RGBA")]
  bc1_RGBA = 130
  #[doc(alias = "MTLPixelFormatBC1_RGBA_sRGB")]
  bc1_RGBA_sRGB = 131
  #[doc(alias = "MTLPixelFormatBC2_RGBA")]
  bc2_RGBA = 132
  #[doc(alias = "MTLPixelFormatBC2_RGBA_sRGB")]
  bc2_RGBA_sRGB = 133
  #[doc(alias = "MTLPixelFormatBC3_RGBA")]
  bc3_RGBA = 134
  #[doc(alias = "MTLPixelFormatBC3_RGBA_sRGB")]
  bc3_RGBA_sRGB = 135
  #[doc(alias = "MTLPixelFormatBC4_RUnorm")]
  bc4_RUnorm = 140
  #[doc(alias = "MTLPixelFormatBC4_RSnorm")]
  bc4_RSnorm = 141
  #[doc(alias = "MTLPixelFormatBC5_RGUnorm")]
  bc5_RGUnorm = 142
  #[doc(alias = "MTLPixelFormatBC5_RGSnorm")]
  bc5_RGSnorm = 143
  #[doc(alias = "MTLPixelFormatBC6H_RGBFloat")]
  bc6H_RGBFloat = 150
  #[doc(alias = "MTLPixelFormatBC6H_RGBUfloat")]
  bc6H_RGBUfloat = 151
  #[doc(alias = "MTLPixelFormatBC7_RGBAUnorm")]
  bc7_RGBAUnorm = 152
  #[doc(alias = "MTLPixelFormatBC7_RGBAUnorm_sRGB")]
  bc7_RGBAUnorm_sRGB = 153
  #[doc(alias = "MTLPixelFormatPVRTC_RGB_2BPP")]
  #[deprecated = "Usage of ASTC/ETC2/BC formats is recommended instead."]
  pvrtc_RGB_2BPP = 160
  #[doc(alias = "MTLPixelFormatPVRTC_RGB_2BPP_sRGB")]
  #[deprecated = "Usage of ASTC/ETC2/BC formats is recommended instead."]
  pvrtc_RGB_2BPP_sRGB = 161
  #[doc(alias = "MTLPixelFormatPVRTC_RGB_4BPP")]
  #[deprecated = "Usage of ASTC/ETC2/BC formats is recommended instead."]
  pvrtc_RGB_4BPP = 162
  #[doc(alias = "MTLPixelFormatPVRTC_RGB_4BPP_sRGB")]
  #[deprecated = "Usage of ASTC/ETC2/BC formats is recommended instead."]
  pvrtc_RGB_4BPP_sRGB = 163
  #[doc(alias = "MTLPixelFormatPVRTC_RGBA_2BPP")]
  #[deprecated = "Usage of ASTC/ETC2/BC formats is recommended instead."]
  pvrtc_RGBA_2BPP = 164
  #[doc(alias = "MTLPixelFormatPVRTC_RGBA_2BPP_sRGB")]
  #[deprecated = "Usage of ASTC/ETC2/BC formats is recommended instead."]
  pvrtc_RGBA_2BPP_sRGB = 165
  #[doc(alias = "MTLPixelFormatPVRTC_RGBA_4BPP")]
  #[deprecated = "Usage of ASTC/ETC2/BC formats is recommended instead."]
  pvrtc_RGBA_4BPP = 166
  #[doc(alias = "MTLPixelFormatPVRTC_RGBA_4BPP_sRGB")]
  #[deprecated = "Usage of ASTC/ETC2/BC formats is recommended instead."]
  pvrtc_RGBA_4BPP_sRGB = 167
  #[doc(alias = "MTLPixelFormatEAC_R11Unorm")]
  eac_R11Unorm = 170
  #[doc(alias = "MTLPixelFormatEAC_R11Snorm")]
  eac_R11Snorm = 172
  #[doc(alias = "MTLPixelFormatEAC_RG11Unorm")]
  eac_RG11Unorm = 174
  #[doc(alias = "MTLPixelFormatEAC_RG11Snorm")]
  eac_RG11Snorm = 176
  #[doc(alias = "MTLPixelFormatEAC_RGBA8")]
  eac_RGBA8 = 178
  #[doc(alias = "MTLPixelFormatEAC_RGBA8_sRGB")]
  eac_RGBA8_sRGB = 179
  #[doc(alias = "MTLPixelFormatETC2_RGB8")]
  etc2_RGB8 = 180
  #[doc(alias = "MTLPixelFormatETC2_RGB8_sRGB")]
  etc2_RGB8_sRGB = 181
  #[doc(alias = "MTLPixelFormatETC2_RGB8A1")]
  etc2_RGB8A1 = 182
  #[doc(alias = "MTLPixelFormatETC2_RGB8A1_sRGB")]
  etc2_RGB8A1_sRGB = 183
  #[doc(alias = "MTLPixelFormatASTC_4x4_sRGB")]
  astc_4x4_sRGB = 186
  #[doc(alias = "MTLPixelFormatASTC_5x4_sRGB")]
  astc_5x4_sRGB = 187
  #[doc(alias = "MTLPixelFormatASTC_5x5_sRGB")]
  astc_5x5_sRGB = 188
  #[doc(alias = "MTLPixelFormatASTC_6x5_sRGB")]
  astc_6x5_sRGB = 189
  #[doc(alias = "MTLPixelFormatASTC_6x6_sRGB")]
  astc_6x6_sRGB = 190
  #[doc(alias = "MTLPixelFormatASTC_8x5_sRGB")]
  astc_8x5_sRGB = 192
  #[doc(alias = "MTLPixelFormatASTC_8x6_sRGB")]
  astc_8x6_sRGB = 193
  #[doc(alias = "MTLPixelFormatASTC_8x8_sRGB")]
  astc_8x8_sRGB = 194
  #[doc(alias = "MTLPixelFormatASTC_10x5_sRGB")]
  astc_10x5_sRGB = 195
  #[doc(alias = "MTLPixelFormatASTC_10x6_sRGB")]
  astc_10x6_sRGB = 196
  #[doc(alias = "MTLPixelFormatASTC_10x8_sRGB")]
  astc_10x8_sRGB = 197
  #[doc(alias = "MTLPixelFormatASTC_10x10_sRGB")]
  astc_10x10_sRGB = 198
  #[doc(alias = "MTLPixelFormatASTC_12x10_sRGB")]
  astc_12x10_sRGB = 199
  #[doc(alias = "MTLPixelFormatASTC_12x12_sRGB")]
  astc_12x12_sRGB = 200
  #[doc(alias = "MTLPixelFormatASTC_4x4_LDR")]
  astc_4x4_LDR = 204
  #[doc(alias = "MTLPixelFormatASTC_5x4_LDR")]
  astc_5x4_LDR = 205
  #[doc(alias = "MTLPixelFormatASTC_5x5_LDR")]
  astc_5x5_LDR = 206
  #[doc(alias = "MTLPixelFormatASTC_6x5_LDR")]
  astc_6x5_LDR = 207
  #[doc(alias = "MTLPixelFormatASTC_6x6_LDR")]
  astc_6x6_LDR = 208
  #[doc(alias = "MTLPixelFormatASTC_8x5_LDR")]
  astc_8x5_LDR = 210
  #[doc(alias = "MTLPixelFormatASTC_8x6_LDR")]
  astc_8x6_LDR = 211
  #[doc(alias = "MTLPixelFormatASTC_8x8_LDR")]
  astc_8x8_LDR = 212
  #[doc(alias = "MTLPixelFormatASTC_10x5_LDR")]
  astc_10x5_LDR = 213
  #[doc(alias = "MTLPixelFormatASTC_10x6_LDR")]
  astc_10x6_LDR = 214
  #[doc(alias = "MTLPixelFormatASTC_10x8_LDR")]
  astc_10x8_LDR = 215
  #[doc(alias = "MTLPixelFormatASTC_10x10_LDR")]
  astc_10x10_LDR = 216
  #[doc(alias = "MTLPixelFormatASTC_12x10_LDR")]
  astc_12x10_LDR = 217
  #[doc(alias = "MTLPixelFormatASTC_12x12_LDR")]
  astc_12x12_LDR = 218
  #[doc(alias = "MTLPixelFormatASTC_4x4_HDR")]
  astc_4x4_HDR = 222
  #[doc(alias = "MTLPixelFormatASTC_5x4_HDR")]
  astc_5x4_HDR = 223
  #[doc(alias = "MTLPixelFormatASTC_5x5_HDR")]
  astc_5x5_HDR = 224
  #[doc(alias = "MTLPixelFormatASTC_6x5_HDR")]
  astc_6x5_HDR = 225
  #[doc(alias = "MTLPixelFormatASTC_6x6_HDR")]
  astc_6x6_HDR = 226
  #[doc(alias = "MTLPixelFormatASTC_8x5_HDR")]
  astc_8x5_HDR = 228
  #[doc(alias = "MTLPixelFormatASTC_8x6_HDR")]
  astc_8x6_HDR = 229
  #[doc(alias = "MTLPixelFormatASTC_8x8_HDR")]
  astc_8x8_HDR = 230
  #[doc(alias = "MTLPixelFormatASTC_10x5_HDR")]
  astc_10x5_HDR = 231
  #[doc(alias = "MTLPixelFormatASTC_10x6_HDR")]
  astc_10x6_HDR = 232
  #[doc(alias = "MTLPixelFormatASTC_10x8_HDR")]
  astc_10x8_HDR = 233
  #[doc(alias = "MTLPixelFormatASTC_10x10_HDR")]
  astc_10x10_HDR = 234
  #[doc(alias = "MTLPixelFormatASTC_12x10_HDR")]
  astc_12x10_HDR = 235
  #[doc(alias = "MTLPixelFormatASTC_12x12_HDR")]
  astc_12x12_HDR = 236
  # A pixel format where the red and green channels are subsampled horizontally.  Two pixels are stored in 32 bits, with shared red and blue values, and unique green values.
  #
  # This format is equivalent to YUY2, YUYV, yuvs, or GL_RGB_422_APPLE/GL_UNSIGNED_SHORT_8_8_REV_APPLE.   The component order, from lowest addressed byte to highest, is Y0, Cb, Y1, Cr.  There is no implicit colorspace conversion from YUV to RGB, the shader will receive (Cr, Y, Cb, 1).  422 textures must have a width that is a multiple of 2, and can only be used for 2D non-mipmap textures.  When sampling, ClampToEdge is the only usable wrap mode.
  #[doc(alias = "MTLPixelFormatGBGR422")]
  gbgr422 = 240
  # A pixel format where the red and green channels are subsampled horizontally.  Two pixels are stored in 32 bits, with shared red and blue values, and unique green values.
  #
  # This format is equivalent to UYVY, 2vuy, or GL_RGB_422_APPLE/GL_UNSIGNED_SHORT_8_8_APPLE. The component order, from lowest addressed byte to highest, is Cb, Y0, Cr, Y1.  There is no implicit colorspace conversion from YUV to RGB, the shader will receive (Cr, Y, Cb, 1).  422 textures must have a width that is a multiple of 2, and can only be used for 2D non-mipmap textures.  When sampling, ClampToEdge is the only usable wrap mode.
  #[doc(alias = "MTLPixelFormatBGRG422")]
  bgrg422 = 241
  # A pixel format where the red and green channels are subsampled horizontally.  Two pixels are stored in 32 bits, with shared red and blue values, and unique green values.
  #
  # This format is equivalent to UYVY, 2vuy, or GL_RGB_422_APPLE/GL_UNSIGNED_SHORT_8_8_APPLE. The component order, from lowest addressed byte to highest, is Cb, Y0, Cr, Y1.  There is no implicit colorspace conversion from YUV to RGB, the shader will receive (Cr, Y, Cb, 1).  422 textures must have a width that is a multiple of 2, and can only be used for 2D non-mipmap textures.  When sampling, ClampToEdge is the only usable wrap mode.
  #[doc(alias = "MTLPixelFormatDepth16Unorm")]
  depth16Unorm = 250
  # A pixel format where the red and green channels are subsampled horizontally.  Two pixels are stored in 32 bits, with shared red and blue values, and unique green values.
  #
  # This format is equivalent to UYVY, 2vuy, or GL_RGB_422_APPLE/GL_UNSIGNED_SHORT_8_8_APPLE. The component order, from lowest addressed byte to highest, is Cb, Y0, Cr, Y1.  There is no implicit colorspace conversion from YUV to RGB, the shader will receive (Cr, Y, Cb, 1).  422 textures must have a width that is a multiple of 2, and can only be used for 2D non-mipmap textures.  When sampling, ClampToEdge is the only usable wrap mode.
  #[doc(alias = "MTLPixelFormatDepth32Float")]
  depth32Float = 252
  # A pixel format where the red and green channels are subsampled horizontally.  Two pixels are stored in 32 bits, with shared red and blue values, and unique green values.
  #
  # This format is equivalent to UYVY, 2vuy, or GL_RGB_422_APPLE/GL_UNSIGNED_SHORT_8_8_APPLE. The component order, from lowest addressed byte to highest, is Cb, Y0, Cr, Y1.  There is no implicit colorspace conversion from YUV to RGB, the shader will receive (Cr, Y, Cb, 1).  422 textures must have a width that is a multiple of 2, and can only be used for 2D non-mipmap textures.  When sampling, ClampToEdge is the only usable wrap mode.
  #[doc(alias = "MTLPixelFormatStencil8")]
  stencil8 = 253
  # A pixel format where the red and green channels are subsampled horizontally.  Two pixels are stored in 32 bits, with shared red and blue values, and unique green values.
  #
  # This format is equivalent to UYVY, 2vuy, or GL_RGB_422_APPLE/GL_UNSIGNED_SHORT_8_8_APPLE. The component order, from lowest addressed byte to highest, is Cb, Y0, Cr, Y1.  There is no implicit colorspace conversion from YUV to RGB, the shader will receive (Cr, Y, Cb, 1).  422 textures must have a width that is a multiple of 2, and can only be used for 2D non-mipmap textures.  When sampling, ClampToEdge is the only usable wrap mode.
  #[doc(alias = "MTLPixelFormatDepth24Unorm_Stencil8")]
  depth24Unorm_Stencil8 = 255
  # A pixel format where the red and green channels are subsampled horizontally.  Two pixels are stored in 32 bits, with shared red and blue values, and unique green values.
  #
  # This format is equivalent to UYVY, 2vuy, or GL_RGB_422_APPLE/GL_UNSIGNED_SHORT_8_8_APPLE. The component order, from lowest addressed byte to highest, is Cb, Y0, Cr, Y1.  There is no implicit colorspace conversion from YUV to RGB, the shader will receive (Cr, Y, Cb, 1).  422 textures must have a width that is a multiple of 2, and can only be used for 2D non-mipmap textures.  When sampling, ClampToEdge is the only usable wrap mode.
  #[doc(alias = "MTLPixelFormatDepth32Float_Stencil8")]
  depth32Float_Stencil8 = 260
  # A pixel format where the red and green channels are subsampled horizontally.  Two pixels are stored in 32 bits, with shared red and blue values, and unique green values.
  #
  # This format is equivalent to UYVY, 2vuy, or GL_RGB_422_APPLE/GL_UNSIGNED_SHORT_8_8_APPLE. The component order, from lowest addressed byte to highest, is Cb, Y0, Cr, Y1.  There is no implicit colorspace conversion from YUV to RGB, the shader will receive (Cr, Y, Cb, 1).  422 textures must have a width that is a multiple of 2, and can only be used for 2D non-mipmap textures.  When sampling, ClampToEdge is the only usable wrap mode.
  #[doc(alias = "MTLPixelFormatX32_Stencil8")]
  x32_Stencil8 = 261
  # A pixel format where the red and green channels are subsampled horizontally.  Two pixels are stored in 32 bits, with shared red and blue values, and unique green values.
  #
  # This format is equivalent to UYVY, 2vuy, or GL_RGB_422_APPLE/GL_UNSIGNED_SHORT_8_8_APPLE. The component order, from lowest addressed byte to highest, is Cb, Y0, Cr, Y1.  There is no implicit colorspace conversion from YUV to RGB, the shader will receive (Cr, Y, Cb, 1).  422 textures must have a width that is a multiple of 2, and can only be used for 2D non-mipmap textures.  When sampling, ClampToEdge is the only usable wrap mode.
  #[doc(alias = "MTLPixelFormatX24_Stencil8")]
  x24_Stencil8 = 262
  # A pixel format where the red and green channels are subsampled horizontally.  Two pixels are stored in 32 bits, with shared red and blue values, and unique green values.
  #
  # This format is equivalent to UYVY, 2vuy, or GL_RGB_422_APPLE/GL_UNSIGNED_SHORT_8_8_APPLE. The component order, from lowest addressed byte to highest, is Cb, Y0, Cr, Y1.  There is no implicit colorspace conversion from YUV to RGB, the shader will receive (Cr, Y, Cb, 1).  422 textures must have a width that is a multiple of 2, and can only be used for 2D non-mipmap textures.  When sampling, ClampToEdge is the only usable wrap mode.
  #[doc(alias = "MTLPixelFormatUnspecialized")]
  unspecialized = 263

