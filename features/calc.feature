# Created by dantas at 02/06/2022
Feature: Calculadora
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

    Scenario Outline: multiplicar dois números
      operação de multiplicação de dois números

    Given o operador 1 é <op1>
    And o operador 2 é <op2>
    When eu multiplico os operadores
    Then o resultado deve ser <resultado>
    Examples:
    |op1  |op2  |resultado|
    |5    |5    |25       |
    |9    |2    |18       |
    |-2    |5   |-10      |

    Scenario Outline: dividir dois números
      operação de divisão de dois números

    Given o operador 1 é <op1>
    And o operador 2 é <op2>
    When eu divido os operadores
    Then o resultado deve ser <resultado>
    Examples:
    |op1  |op2  |resultado|
    |10   |2    |5        |
    |200  |20   |10       |
    |1    |1    |1        |

    Scenario Outline: potencia de dois números
      operação de potenciação de dois números

    Given o operador 1 é <op1>
    And o operador 2 é <op2>
    When eu elevo um operador pelo outro
    Then o resultado deve ser <resultado>
    Examples:
    |op1  |op2  |resultado|
    |2    |4    |16       |
    |5    |3    |125      |
    |10   |3    |1000     |
