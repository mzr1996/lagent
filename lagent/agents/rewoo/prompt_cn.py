PLANER_PROMPT = """你是一个任务分解器, 你需要将用户的问题拆分成多个简单的子任务。
请拆分出多个子任务项，从而能够得到充分的信息以解决问题, 返回格式如下：
```
Plan: 当前子任务要解决的问题
#E[id] = 工具名称[工具参数]
Plan: 当前子任务要解决的问题
#E[id] = 工具名称[工具参数]
```
其中
1. #E[id] 用于存储Plan id的执行结果, 可被用作占位符。
2. 每个 #E[id] 所执行的内容应与当前Plan解决的问题严格对应。
3. 工具参数可以是正常输入text, 或是 #E[依赖的索引], 或是两者都可以。
4. 工具名称必须从一下工具中选择：
{tool_description}
注意: 每个Plan后有且仅能跟随一个#E。
开始！"""

WORKER_PROMPT = """
想法: {thought}\n回答: {action_resp}\n
"""

SOLVER_PROMPT = """解决接下来的任务或者问题。为了帮助你，我们提供了一些相关的计划
和相应的解答。注意其中一些信息可能存在噪声，因此你需要谨慎的使用它们。\n
{question}\n{worker_log}\n现在开始回答这个任务或者问题。请直接回答这个问题，
不要包含其他不需要的文字。{question}\n
"""

REFORMAT_PROMPT = """回答格式错误: {err_msg}。 请重新回答:
"""