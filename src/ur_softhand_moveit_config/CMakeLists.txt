cmake_minimum_required(VERSION 3.22)
project(ur_softhand_moveit_config)

find_package(ament_cmake REQUIRED)

ament_package()

# Instalar archivos de lanzamiento
install(
  DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
  PATTERN "setup_assistant.launch" EXCLUDE)

# Instalar configuraciones
install(DIRECTORY config DESTINATION share/${PROJECT_NAME})

# Instalar archivo .setup_assistant
install(FILES .setup_assistant DESTINATION share/${PROJECT_NAME})

# Instalar script merge.py como ejecutable
install(
  PROGRAMS scripts/merge.py
  DESTINATION lib/${PROJECT_NAME}
)
