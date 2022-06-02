from behave import *
from src.main import Calculator
# use_step_matcher("re")


@given("o operador 1 é {op1}")
def set_op1(context, op1):
    """
    :type context: behave.runner.Context
    """
    context.op1 = int(op1)


@step("o operador 2 é {op2}")
def set_op2(context, op2):
    """
    :type context: behave.runner.Context
    """
    context.op2 = int(op2)


@when("eu somo os operadores")
def soma(context):
    """
    :type context: behave.runner.Context
    """
    calc = Calculator()
    context.resultado = calc.sum(context.op1, context.op2)


@when("eu subtraio os operadores")
def subtracao(context):
    """
    :type context: behave.runner.Context
    """
    calc = Calculator()
    context.resultado = calc.sub(context.op1, context.op2)


@when("eu multiplico os operadores")
def multiplicacao(context):
    """
    :type context: behave.runner.Context
    """
    calc = Calculator()
    context.resultado = calc.mult(context.op1, context.op2)


@when("eu divido os operadores")
def divisao(context):
    """
    :type context: behave.runner.Context
    """
    calc = Calculator()
    context.resultado = calc.div(context.op1, context.op2)


@when("eu elevo um operador pelo outro")
def poteciacao(context):
    """
    :type context: behave.runner.Context
    """
    calc = Calculator()
    context.resultado = calc.pot(context.op1, context.op2)


@then("o resultado deve ser {resultado}")
def result(context, resultado):
    """
    :type context: behave.runner.Context
    """
    assert context.resultado == int(resultado)
