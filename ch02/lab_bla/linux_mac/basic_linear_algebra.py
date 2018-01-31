def vector_size_check(*vector_variables):
    last_value = -1;
    for vector in vector_variables:
        value = len(vector)
        if last_value == -1:
            last_value = value
            continue
        if value != last_value:
            return False
        last_value = value;
    return True;

def vector_addition(*vector_variables):
    return sum(vector_variables)


def vector_subtraction(*vector_variables):
    if not vector_size_check(*vector_variables):
        raise ArithmeticError
    return -1*sum(vector_variables)


def scalar_vector_product(alpha, vector_variable):
    return alpha*vector_variable


def matrix_size_check(*matrix_variables):
    return None


def is_matrix_equal(*matrix_variables):
    return None


def matrix_addition(*matrix_variables):
    if not matrix_size_check(*matrix_variables):
        raise ArithmeticError
    return None


def matrix_subtraction(*matrix_variables):
    if not matrix_size_check(*matrix_variables):
        raise ArithmeticError
    return None


def matrix_transpose(matrix_variable):
    return None


def scalar_matrix_product(alpha, matrix_variable):
    return None


def is_product_availability_matrix(matrix_a, matrix_b):
    return None


def matrix_product(matrix_a, matrix_b):
    if not is_product_availability_matrix(matrix_a, matrix_b):
        raise ArithmeticError
    return None
