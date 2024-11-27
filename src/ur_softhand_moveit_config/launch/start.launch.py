from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_demo_launch
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # Configuración de MoveIt
    moveit_config = MoveItConfigsBuilder("my_robot_cell", package_name="ur_softhand_moveit_config").to_moveit_configs()
    
    # Nodo que ejecuta el merge de estados de articulaciones
    merge_node = Node(
        package='ur_softhand_moveit_config',  # Nombre del paquete
        executable='merge.py',               # Nombre del archivo ejecutable
        name='joint_state_merger',           # Nombre del nodo
        output='screen'                      # Mostrar salida en pantalla
    )

    # Generar lanzamiento de demo de MoveIt
    demo_launch = generate_demo_launch(moveit_config)

    # Retornar la descripción del lanzamiento con el nodo de merge y el demo
    return LaunchDescription([merge_node, *demo_launch.entities])
