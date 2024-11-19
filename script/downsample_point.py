# cook_spinach原始colmap生成的点云数量924016,降采样后为93172
# 使用方法----------------------------------------------------------------------------
# python script/downsample_point.py \
# <location>/<scene>/colmap/dense/workspace/fused.ply \
# <location>/<scene>/points3D_downsample.ply
# 
# $ python script/downsample_point.py \
# /home/ekko/datasets/Neural_3D_Video/cook_spinach/colmap/dense/workspace/fused.ply \
# /home/ekko/datasets/Neural_3D_Video/cook_spinach/points3D_downsample.ply
# 
import open3d as o3d
import sys
def process_ply_file(input_file, output_file):
    pcd = o3d.io.read_point_cloud(input_file)
    print(f"Total points: {len(pcd.points)}")

    voxel_size=0.001
    while len(pcd.points) > 100000:
        # https://www.open3d.org/docs/0.14.1/tutorial/geometry/pointcloud.html
        pcd = pcd.voxel_down_sample(voxel_size=voxel_size)
        print(f"Downsampled points: {len(pcd.points)}")
        voxel_size+=0.005

    o3d.io.write_point_cloud(output_file, pcd)

process_ply_file(sys.argv[1], sys.argv[2])