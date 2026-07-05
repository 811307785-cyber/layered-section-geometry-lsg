"""
显微成像噪声优化模块（场景专属）
底层依赖：Common-LSG constraint_algo 平滑算子
功能：抑制散粒噪声、光漂白效应，保留生物结构细节
"""
from Common_LSG.constraint_algo import AdaptiveSmoother

class MicroscopeNoiseOptimize(AdaptiveSmoother):
    def shot_noise_suppress(self, section_matrix):
        """光子散粒噪声抑制"""
        denoised_matrix = self.poisson_noise_filter(section_matrix)
        return denoised_matrix

    def photobleaching_correct(self, section_stack):
        """光漂白效应校正，平衡层间亮度差异"""
        corrected_stack = self.layer_brightness_balance(section_stack)
        return corrected_stack