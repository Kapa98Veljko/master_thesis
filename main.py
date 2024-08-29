def calculate_line_delay(length):
    # Delay calculation based on line length
    return (1.5 / 0.3) * length  # in nanoseconds

def calculate_tlt(T, lengths):
    # Calculate cumulative TLT for nth device as sum of all transceivers and line delays
    cumulative_tlt = 0
    for length in lengths:
        L = calculate_line_delay(length)
        cumulative_tlt += 2 * T + L  # 2*T for two transceivers + L for line
    return cumulative_tlt

def calculate_device_delay(index, p, tlt):
    if index == 1:
        return 3 * p + 2 * tlt
    else:
        return 2 * index * (p + tlt)

def simulate_enumeration(p, T, lengths):
    total_delay = 0
    device_delays = []
    
    for i in range(1, len(lengths) + 1):
        # For each device i, sum up TLT from the master to this device
        tlt = calculate_tlt(T, lengths[:i])
        delay = calculate_device_delay(i, p, tlt)
        device_delays.append(delay)
        total_delay += delay
    
    return total_delay, device_delays

# Example parameters
p = 500  # nanoseconds, processor delay
T = 100  # nanoseconds, transceiver propagation delay
lengths = [100, 150, 200]  # in cm, example lengths of the lines between devices

total_delay, delays = simulate_enumeration(p, T, lengths)
print(f"Total delay for all devices: {total_delay} ns")
for idx, delay in enumerate(delays, start=1):
    print(f"Device {idx} delay: {delay} ns")
