class Polynomial:
    def __init__(self, coefficients=None):
        if coefficients is None:
            self.coefficients = []
        else:
            self.coefficients = coefficients

    def __repr__(self):
        terms = []
        for exp, coeff in enumerate(self.coefficients[::-1]):
            if coeff != 0:
                term = f"{coeff}x^{exp}" if exp else f"{coeff}"
                terms.append(term)
        return " + ".join(terms) or "0"

    def __add__(self, other):
        max_len = max(len(self.coefficients), len(other.coefficients))
        result = [0] * max_len
        for exp, coeff in enumerate(self.coefficients):
            result[exp] += coeff
        for exp, coeff in enumerate(other.coefficients):
            result[exp] += coeff
        return Polynomial(result)

    def __mul__(self, other):
        result = [0] * (len(self.coefficients) + len(other.coefficients) - 1)
        for i, coeff1 in enumerate(self.coefficients):
            for j, coeff2 in enumerate(other.coefficients):
                result[i + j] += coeff1 * coeff2
        return Polynomial(result)
#مثال 
poly1 = Polynomial([1, 2, 3])  # 3x^2 + 2x + 1
poly2 = Polynomial([4, -1])    # -x + 4

print("Polynomial 1:", poly1)
print("Polynomial 2:", poly2)

sum_poly = poly1 + poly2
print("Sum:", sum_poly)

product_poly = poly1 * poly2
print("Product:", product_poly)