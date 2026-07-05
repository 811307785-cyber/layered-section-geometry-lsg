"""
工业缺陷边界约束模块（场景专属）
底层依赖：Common-LSG constraint_algo 基类
功能：微小尺度缺陷边界精准提取，强化细层级截面分辨率
"""
from Common_LSG.constraint_algo import BaseSectionConstraint

class DefectBoundaryConstraint(BaseSectionConstraint):
    def micro_defect_enhance(self, section_matrix, defect_size_min=0.1):
        """微小缺陷边界增强，提升细层级缺陷检出率"""
        enhanced_matrix = self.subpixel_edge_enhance(section_matrix, min_size=defect_size_min)
        return enhanced_matrix

    def workpiece_geometry_constrain(self, section_matrix, workpiece_type="casting"):
        """工件几何形状约束，排除非缺陷异常梯度"""
        geometry_template = self.get_standard_geometry(workpiece_type)
        constrained_matrix = self.template_boundary_constrain(section_matrix, geometry_template)
        return constrained_matrix