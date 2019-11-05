import sys
import container_functions as cf

# Default state is Production, indicated by 0
# 1 represents an ongoing test
SYSTEM_STATE = 0
# Variable to hold current containers in a list
current_containers = []
# Port mappings
BASE_PORT = 8081

# router table

"""
This method checks if any container from our image is running
on the host currently
"""


def number_of_containers_running():
    return len(cf.check_container_status_and_get(cf.IMAGE_NAME))


"""
This method attempts to start the system in Production mode, exiting
if that is not possible with a non-zero exit code
"""


def start_system():
    current_containers = cf.start_and_get_containers(
        cf.get_latest_image(), 8082, BASE_PORT)
    if current_containers == []:
        print('Critical error, system unable to start as no containers could be run')
        sys.exit(1)
    else:
        print('System has started successfully!')


"""
###
"""


def is_test_running():
    return number_of_containers_running() == 2


def start_test(test_image, host_port, container_port):
    if is_test_running():
        return True
    else:
        cf.start_and_get_containers(
            test_image, host_port, container_port, True)
        current_containers = cf.check_container_status_and_get(cf.IMAGE_NAME)
        return True


def stop_test(is_successful):
    if is_successful:
        # Kill production, switch to test
        pass
    else:
        # Kill test, switch to production
        pass
    SYSTEM_STATE = 0


"""
Placeholder method for parsing test config
"""


def parse_test_config(req):
    try:
        # Current state checking
        # Parse params
        #duration = int(req['duration'])
        #test_type = req['A/BTest']

        # Create container, switch state and update test params
        return True
    except:
        # State shall remain unchanged
        return False

        #     {
        #     "DeploymentId": "1",
        #     "DeploymentType": "A/BTest",
        #     "DeploymentParam": {
        #       "Duration": 135
        #     },
        #     "ModelInfo":
        #     [
        #       {
        #         "ModelContainerName": "container1",
        #         "UserRange": 0.2
        #       },
        #       {
        #         "ModelContainerName": "container2",
        #         "UserRange": 0.8
        #       }
        #     ]

        # }