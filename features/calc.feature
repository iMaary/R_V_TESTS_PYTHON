# Created by danta at 31/05/2022
Feature: CalculadoraA
  # Enter feature description here

  Scenario Outline: somar dois números
    operação de soma de dois números

    Given o operador 1 é <op1>
    And o operador 2 é <op2>
    When eu somo os operadores
    Then o resultado deve ser <resultado>
    Examples:
    |op1  |op2  |resultado  |
    |2    |4    |6          |
    |3    |7    |10         |
    |8    |6    |14         |

  Scenario Outline: subtrair dois números
    operação de subtrai de dois números

    Given o operador 1 é <op1>
    And o operador 2 é <op2>
    When eu subtraio os operadores
    Then o resultado deve ser <resultado>
    Examples:
    |op1  |op2  |resultado|
    |2    |4    |-2       |
    |3    |7    |-4       |
    |8    |6    |2        |