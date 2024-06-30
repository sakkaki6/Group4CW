import platform

class EnvironmentInfo:
    @classmethod
    def get_os_info(cls):
        os_info = {
            "system": platform.system(),
            "node": platform.node(),
            "release": platform.release(),
            "version": platform.version(),
            "machine": platform.machine(),
            "processor": platform.processor()
        }
        return os_info


os_info = EnvironmentInfo.get_os_info()
print(os_info)
