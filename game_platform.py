def speed_after_unit(start_speed: int, unit_speed: int) -> int:
    return start_speed - unit_speed

def calculate_final_speed(initial_speed, inclinations) -> int:
    last_speed = initial_speed
    for i in inclinations:
        last_speed = speed_after_unit(last_speed, i)
        if last_speed <= 0:
            return 0
    
    return last_speed
    

print(calculate_final_speed(60, [0, 30, 0, -45, 0]))