from fractions import gcd

def answer(vertices):
    xa, xb, xc = [x[0] for x in vertices]
    ya, yb ,yc = [x[1] for x in vertices]

    # Compute area with Shoelace formula
    area = 0.5 * abs((xa - xc) * (yb - ya) - (xa - xb) * (yc - ya))

    # Points on boundries
    boundry_points = gcd(abs(xa - xb), abs(ya - yb)) + gcd(abs(xb - xc), abs(yb - yc)) + gcd(abs(xc - xa), abs(yc - ya))

    #Pick's theorem
    points = area - boundry_points/2 + 1

    return int(points)