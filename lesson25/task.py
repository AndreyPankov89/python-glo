from pyowm.owm import OWM
owm = OWM('2992f4fa8670a7ae1ce7f58c4777326e')
mgr = owm.weather_manager()
observation = mgr.weather_at_place('Moscow,RU')
print(observation.weather.temperature('celsius')['temp'])