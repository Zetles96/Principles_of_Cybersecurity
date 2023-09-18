import numpy as np


# Trial division that calculates p and q for the RSA key.
def trial_division(N: int) -> list[int]:
    factor_N = []
    # Checks if N is divisible by two, and then appends 2 to the factors
    while N % 2 == 0:
        factor_N.append(2)
        N //= 2
    # Sets the factor_guess to 3 afterwards
    factor_guess = 3
    # Checks if the trial is within the limit
    while factor_guess * factor_guess <= N:
        # Checks if the factor guess is a factor of N
        if N % factor_guess == 0:
            # Add the factor
            factor_N.append(factor_guess)
            # Divides out the factor
            N //= factor_guess
        else:
            # Increments the guess
            factor_guess += 2
    # finds the second / last factor of N
    if N != 1:
        factor_N.append(N)
    print(f"The factors p and q is {factor_N}")
    return factor_N


# Extended euclidian algorithm for calculating d for the rsa key.
def extended_euclidian_algorithm(e: int, p: int, q: int) -> int:
    phi = (p - 1) * (q - 1)
    b = phi
    e = np.abs(e)
    b = np.abs(b)
    i = [-1, 0]
    r_i = np.array([e, b], dtype=np.int64)
    q_i = np.array([0, 0], dtype=np.int64)
    s_i = np.array([1, 0], dtype=np.int64)
    t_i = np.array([0, 1], dtype=np.int64)
    while b != 0:
        r = e % b
        q = int(e / b)
        q_i = np.append(q_i, q)
        s = s_i[-2] - q_i[-1] * s_i[-1]
        t = t_i[-2] - q_i[-1] * t_i[-1]
        e = b
        b = r
        i = np.append(i, (i[-1]) + 1)
        r_i = np.append(r_i, r)
        s_i = np.append(s_i, s)
        t_i = np.append(t_i, t)
    d = int(phi + s_i[-2])
    print(f"Decryption key d is {d}")
    return d


# Enc algorithm for RSA
def enc(m: int, e: int, N: int) -> int:
    return pow(m, e, N)


# Dec algorithm for RSA
def dec(c: int, d: int, N: int) -> int:
    m = pow(c, d, N)
    print(f"The message is {m}")
    return m


# should crack the RSA and give the message
def crack(c: int, e: int, N: int) -> int:
    p, q = trial_division(N=N)
    d = extended_euclidian_algorithm(e=e, p=p, q=q)
    return dec(c=c, d=d, N=N)


if __name__ == '__main__':
    c, e, N = 17, (2 ** 16 + 1), 4294967317
    if enc(crack(c=c, e=e, N=N), e=e, N=N) == c:
        print("You broke the key ╰(*°▽°*)╯ since c* = c")
