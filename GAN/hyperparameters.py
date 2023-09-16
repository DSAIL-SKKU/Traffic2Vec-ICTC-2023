from lib.algos.sigcwgan import SigCWGANConfig
from lib.augmentations import get_standard_augmentation, SignatureConfig, Scale, Concat, Cumsum, AddLags, LeadLag

SIGCWGAN_CONFIGS = dict(
    ECG=SigCWGANConfig(
        mc_size=1000,
        sig_config_past=SignatureConfig(depth=2, augmentations=get_standard_augmentation(0.05)),
        sig_config_future=SignatureConfig(depth=2, augmentations=get_standard_augmentation(0.05)),
    ),
    
    
    interactive=SigCWGANConfig(
        mc_size=1000,
        sig_config_past=SignatureConfig(depth=2, augmentations=get_standard_augmentation(0.05)),
        sig_config_future=SignatureConfig(depth=2, augmentations=get_standard_augmentation(0.05)),
    ),
    bulk=SigCWGANConfig(
        mc_size=1000,
        sig_config_past=SignatureConfig(depth=2, augmentations=get_standard_augmentation(0.05)),
        sig_config_future=SignatureConfig(depth=2, augmentations=get_standard_augmentation(0.05)),
    ),
    video=SigCWGANConfig(
        mc_size=1000,
        sig_config_past=SignatureConfig(depth=2, augmentations=get_standard_augmentation(0.05)),
        sig_config_future=SignatureConfig(depth=2, augmentations=get_standard_augmentation(0.05)),
    ),
    web=SigCWGANConfig(
        mc_size=1000,
        sig_config_past=SignatureConfig(depth=2, augmentations=get_standard_augmentation(0.05)),
        sig_config_future=SignatureConfig(depth=2, augmentations=get_standard_augmentation(0.05)),
    ),
    
    
    
    interactive_emb=SigCWGANConfig(
        mc_size=1000,
        sig_config_past=SignatureConfig(depth=2, augmentations=get_standard_augmentation(0.05)),
        sig_config_future=SignatureConfig(depth=2, augmentations=get_standard_augmentation(0.05)),
    ),
    bulk_emb=SigCWGANConfig(
        mc_size=1000,
        sig_config_past=SignatureConfig(depth=2, augmentations=get_standard_augmentation(0.05)),
        sig_config_future=SignatureConfig(depth=2, augmentations=get_standard_augmentation(0.05)),
    ),
    video_emb=SigCWGANConfig(
        mc_size=1000,
        sig_config_past=SignatureConfig(depth=2, augmentations=get_standard_augmentation(0.05)),
        sig_config_future=SignatureConfig(depth=2, augmentations=get_standard_augmentation(0.05)),
    ),
    web_emb=SigCWGANConfig(
        mc_size=1000,
        sig_config_past=SignatureConfig(depth=2, augmentations=get_standard_augmentation(0.05)),
        sig_config_future=SignatureConfig(depth=2, augmentations=get_standard_augmentation(0.05)),
    ),
    
    
    
    GEANT=SigCWGANConfig(
        mc_size=1000,
        sig_config_past=SignatureConfig(depth=2, augmentations=get_standard_augmentation(0.05)),
        sig_config_future=SignatureConfig(depth=2, augmentations=get_standard_augmentation(0.05)),
    ),
    Abilene=SigCWGANConfig(
        mc_size=1000,
        sig_config_past=SignatureConfig(depth=2, augmentations=get_standard_augmentation(0.05)),
        sig_config_future=SignatureConfig(depth=2, augmentations=get_standard_augmentation(0.05)),
    ),
    
    GEANT_emb=SigCWGANConfig(
        mc_size=1000,
        sig_config_past=SignatureConfig(depth=2, augmentations=get_standard_augmentation(0.05)),
        sig_config_future=SignatureConfig(depth=2, augmentations=get_standard_augmentation(0.05)),
    ),
    Abilene_emb=SigCWGANConfig(
        mc_size=1000,
        sig_config_past=SignatureConfig(depth=2, augmentations=get_standard_augmentation(0.05)),
        sig_config_future=SignatureConfig(depth=2, augmentations=get_standard_augmentation(0.05)),
    ),
    
    
    
    
    VAR1=SigCWGANConfig(
        mc_size=500,
        sig_config_past=SignatureConfig(depth=3, augmentations=tuple([Scale(0.2), Cumsum(), AddLags(m=2), LeadLag()])),
        sig_config_future=SignatureConfig(depth=3,
                                          augmentations=tuple([Scale(0.2), Cumsum(), AddLags(m=2), LeadLag()])),
    ),
    VAR2=SigCWGANConfig(
        mc_size=1000,
        sig_config_past=SignatureConfig(depth=2, augmentations=get_standard_augmentation(0.2)),
        sig_config_future=SignatureConfig(depth=2, augmentations=get_standard_augmentation(0.2)),
    ),
    VAR3=SigCWGANConfig(
        mc_size=1000,
        sig_config_past=SignatureConfig(depth=2, augmentations=get_standard_augmentation(0.2)),
        sig_config_future=SignatureConfig(depth=2, augmentations=get_standard_augmentation(0.2)),
    ),
    VAR20=SigCWGANConfig(
        mc_size=2000,
        sig_config_past=SignatureConfig(depth=2, augmentations=(Scale(0.5), Cumsum(), Concat())),
        sig_config_future=SignatureConfig(depth=2, augmentations=(Scale(0.5), Cumsum(), Concat())),
    ),
    STOCKS_SPX=SigCWGANConfig(
        mc_size=1000,
        sig_config_past=SignatureConfig(depth=3, augmentations=tuple([Scale(0.2), Cumsum(), AddLags(m=2), LeadLag()])),
        sig_config_future=SignatureConfig(depth=3,
                                          augmentations=tuple([Scale(0.2), Cumsum(), AddLags(m=2), LeadLag()])),
    ),
    STOCKS_SPX_DJI=SigCWGANConfig(
        mc_size=1000,
        sig_config_past=SignatureConfig(depth=2, augmentations=tuple([Scale(0.2), Cumsum(), AddLags(m=2), LeadLag()])),
        sig_config_future=SignatureConfig(depth=2,
                                          augmentations=tuple([Scale(0.2), Cumsum(), AddLags(m=2), LeadLag()])),
    ),
    ARCH=SigCWGANConfig(
        mc_size=2000,
        sig_config_past=SignatureConfig(depth=3, augmentations=get_standard_augmentation(0.2)),
        sig_config_future=SignatureConfig(depth=3, augmentations=get_standard_augmentation(0.2)),
    ),
)
