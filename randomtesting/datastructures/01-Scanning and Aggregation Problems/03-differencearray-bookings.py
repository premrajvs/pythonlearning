def corpFlightBookings(bookings, n):
    diff = [0] * n
    
    for first, last, seats in bookings:
        diff[first - 1] += seats
        
        if last < n:
            diff[last] -= seats
    
    # Build final result using prefix sum
    for i in range(1, n):
        diff[i] += diff[i - 1]
    
    return diff