"""
建筑BIM逆向建模Demo
"""
from Architecture_BIM.hardware_adapt.tilt_photography_parser import TiltPhotographyParser
from Architecture_BIM.noise_optimize.pointcloud_dynamic_denoise import BuildingPointCloudDenoise
from Architecture_BIM.scene_constraint.building_structure_constraint import BuildingStructureConstraint
from Common_LSG.slice_rebuild import SectionRebuilder

def bim_rebuild_pipeline(las_path, output_path):
    parser = TiltPhotographyParser()
    building_data = parser.load_pointcloud_las(las_path)
    
    denoiser = BuildingPointCloudDenoise()
    cleaned_stack = denoiser.dynamic_object_remove(building_data.section_stack)
    
    constraint = BuildingStructureConstraint()
    constrained_stack = [constraint.orthogonal_structure_constrain(s) for s in cleaned_stack]
    
    rebuilder = SectionRebuilder()
    bim_model = rebuilder.non_orthogonal_rebuild(constrained_stack, building_data.spacing)
    
    print("建筑BIM逆向三维建模完成")
    return bim_model

if __name__ == "__main__":
    bim_rebuild_pipeline("./building.las", "./output/bim_model.stl")