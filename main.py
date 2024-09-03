def calculate_line_delay(length):
    # Delay calculation based on line length
    return (1.5 / 0.3) * length  # in nanoseconds

def calculate_tlt(T, lengths):
    # Calculate cumulative TLT for a device as the sum of TLT for all previous devices
    cumulative_tlt = 0
    for length in lengths:
        L = calculate_line_delay(length)
        cumulative_tlt += 2 * T + L  # 2*T for two transceivers + L for line
    return cumulative_tlt

def calculate_first_device_delay(p, tlt):
    # t1 = 5 * p + 4 * TLT (with correct TLT definition)
    return 5 * p + tlt

def calculate_nth_device_delay(p, tlt):
    # tn = 4 * p  + TLT (with correct TLT definition)
    return 4 * p + tlt

def simulate_architecture(p, T, lengths):
    total_delay = 0
    device_delays = []
    
    for i in range(1, len(lengths) + 1):
        # Calculate cumulative TLT for the nth device considering all previous devices
        tlt = 4*calculate_tlt(T, lengths[:i])
        print("tlt = ",tlt)
        if i == 1:
            delay = calculate_first_device_delay(p, tlt)
        else:
            print(tlt)
            delay = calculate_nth_device_delay(p, tlt)
        
        device_delays.append(delay)
        total_delay += delay
    
    return total_delay, device_delays

# Example parameters
p = 500  # nanoseconds, processor delay
T = 100  # nanoseconds, transceiver propagation delay
lengths = [100, 150, 200]  # in cm, example lengths of the lines between devices

total_delay, delays = simulate_architecture(p, T, lengths)
print(f"Total delay for all devices: {total_delay} ns")
for idx, delay in enumerate(delays, start=1):
    print(f"Device {idx} delay: {delay} ns")
