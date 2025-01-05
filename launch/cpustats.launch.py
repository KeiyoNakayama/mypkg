import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():
    check_cpu_stats = launch_ros.actions.Node(
            package = 'mypkg',
            executable = 'check_cpu_stats',
            )

    wifispeed_listner = launch_ros.actions.Node(
            package = 'mypkg',
            executable = 'cpustats_listner',
            output = 'screen'
            )

    return launch.LaunchDescription([check_cpu_stats, cpustats_listner])
