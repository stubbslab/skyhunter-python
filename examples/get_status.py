from skyhunter import IoptronMount
from config import port

# Example usage
mount = IoptronMount(port)
status = mount.get_system_state()
