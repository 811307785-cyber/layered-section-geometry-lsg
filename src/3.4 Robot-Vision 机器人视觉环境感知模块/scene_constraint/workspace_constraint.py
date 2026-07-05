"""
机器人工作空间约束模块（场景专属）
底层依赖：Common-LSG constraint_algo 基类
功能：限定机器人工作空间范围，提取避障层级，适配嵌入式低算力场景
"""
from Common_LSG.constraint_algo import BaseSectionConstraint

class WorkspaceConstraint(BaseSectionConstraint):
    def workspace_range_constrain(self, section_matrix, workspace_boundary):
        """工作空间范围约束，裁剪无效区域，降低计算量"""
        constrained_matrix = self.boundary_clip(section_matrix, workspace_boundary)
        return constrained_matrix

    def obstacle_layer_extract(self, section_stack, safety_distance=0.1):
        """障碍物层级提取，输出避障专用层级数据"""
        obstacle_layers = self.distance_layer_segment(section_stack, safety_distance=safety_distance)
        return obstacle_layers