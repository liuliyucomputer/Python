# 2. 语法分析：构建抽象语法树(AST)
import ast

source_code = "x = 1 + 2"
ast_tree = ast.parse(source_code)
print("抽象语法树:")
print(ast.dump(ast_tree, indent=2))