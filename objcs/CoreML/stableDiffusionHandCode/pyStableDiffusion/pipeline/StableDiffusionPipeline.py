class _StableDiffusionPipeline:
  def __init__(self):
    self.textEncoder: TextEncoder
    self.unet: Unet
    self.decoder: Decoder
    self.safetyChecker: SafetyChecker
    self.reduceMemory: bool = False

  def init_textEncoder_unet_decoder_safetyChecker_reduceMemory(
      self, textEncoder, unet, decoder, safetyChecker, reduceMemory):
    self.textEncoder = textEncoder
    self.unet = unet
    self.decoder = decoder
    self.safetyChecker = safetyChecker
    self.reduceMemory = reduceMemory

  def generateImages(self,
                     prompt: str,
                     negativePrompt: str='',
                     imageCount: int=1,
                     stepCount: int=50,
                     seed: int=0,
                     guidanceScale: float=7.5,
                     disableSafety: bool=False):
    self.promptEmbedding = self.textEncoder.encode()

