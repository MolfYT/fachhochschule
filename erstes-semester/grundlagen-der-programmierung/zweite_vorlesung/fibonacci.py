def fibonacci_stelle(stelle_der_folge):
    if stelle_der_folge < 1: 
        return 0
    elif stelle_der_folge == 1:
        return 1
    elif stelle_der_folge == 2:
        return 2
    else:
        return fibonacci_stelle(stelle_der_folge-2) + fibonacci_stelle(stelle_der_folge-1)