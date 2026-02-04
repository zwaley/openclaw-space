import random
import time
import os

class SnakeGame:
    def __init__(self, width=20, height=15):
        self.width = width
        self.height = height
        self.snake = [(width//2, height//2)]  # 蛇的初始位置
        self.direction = 'RIGHT'  # 初始方向
        self.food = self.generate_food()
        self.score = 0
        self.game_over = False
    
    def generate_food(self):
        """生成食物，确保不在蛇身上"""
        while True:
            food = (random.randint(0, self.width-1), random.randint(0, self.height-1))
            if food not in self.snake:
                return food
    
    def move_snake(self):
        """移动蛇"""
        head_x, head_y = self.snake[0]
        
        if self.direction == 'UP':
            new_head = (head_x, head_y - 1)
        elif self.direction == 'DOWN':
            new_head = (head_x, head_y + 1)
        elif self.direction == 'LEFT':
            new_head = (head_x - 1, head_y)
        elif self.direction == 'RIGHT':
            new_head = (head_x + 1, head_y)
        
        # 检查是否撞墙
        if (new_head[0] < 0 or new_head[0] >= self.width or 
            new_head[1] < 0 or new_head[1] >= self.height):
            self.game_over = True
            return
        
        # 检查是否撞到自己
        if new_head in self.snake:
            self.game_over = True
            return
        
        # 移动蛇头
        self.snake.insert(0, new_head)
        
        # 检查是否吃到食物
        if new_head == self.food:
            self.score += 10
            self.food = self.generate_food()
        else:
            # 如果没吃到食物，移除尾巴
            self.snake.pop()
    
    def draw_board(self):
        """绘制游戏界面"""
        os.system('cls' if os.name == 'nt' else 'clear')  # 清屏
        
        # 创建游戏面板
        board = [[' ' for _ in range(self.width)] for _ in range(self.height)]
        
        # 放置蛇的身体
        for i, (x, y) in enumerate(self.snake):
            if i == 0:  # 蛇头
                board[y][x] = 'O'
            else:  # 蛇身
                board[y][x] = 'o'
        
        # 放置食物
        food_x, food_y = self.food
        board[food_y][food_x] = '@'
        
        # 绘制边框和内容
        print('+' + '-' * (self.width * 2 + 1) + '+')
        for row in board:
            print('| ' + ' '.join(row) + ' |')
        print('+' + '-' * (self.width * 2 + 1) + '+')
        
        print(f"分数: {self.score}")
        print("使用 w/a/s/d 控制方向，q 退出游戏")
    
    def change_direction(self, key):
        """改变方向"""
        if key == 'w' and self.direction != 'DOWN':
            self.direction = 'UP'
        elif key == 's' and self.direction != 'UP':
            self.direction = 'DOWN'
        elif key == 'a' and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        elif key == 'd' and self.direction != 'LEFT':
            self.direction = 'RIGHT'
        elif key == 'q':
            self.game_over = True

def main():
    game = SnakeGame()
    
    print("欢迎来到贪吃蛇游戏！")
    print("按任意键开始...")
    input()
    
    try:
        while not game.game_over:
            game.draw_board()
            game.move_snake()
            
            if game.game_over:
                break
            
            # 获取用户输入
            import select
            import sys
            
            # 非阻塞输入检测
            if os.name == 'nt':  # Windows
                import msvcrt
                if msvcrt.kbhit():
                    key = msvcrt.getch().decode('utf-8').lower()
                    game.change_direction(key)
            else:  # Unix/Linux/Mac
                if select.select([sys.stdin], [], [], 0.1)[0]:
                    key = sys.stdin.read(1).lower()
                    game.change_direction(key)
            
            time.sleep(0.2)  # 控制游戏速度
    
    except KeyboardInterrupt:
        pass
    
    print("\n游戏结束！")
    print(f"最终得分: {game.score}")

# 简化版本，适用于所有平台
def simple_main():
    game = SnakeGame()
    
    print("欢迎来到贪吃蛇游戏！")
    print("按 Enter 开始...")
    input()
    
    import sys
    import tty
    import termios
    
    old_settings = termios.tcgetattr(sys.stdin)
    
    try:
        while not game.game_over:
            game.draw_board()
            game.move_snake()
            
            if game.game_over:
                break
            
            # 尝试获取输入
            print("请输入命令 (w/a/s/d/q): ", end='', flush=True)
            
            # 使用原始模式获取单字符输入
            tty.setraw(sys.stdin.fileno())
            key = sys.stdin.read(1).lower()
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
            
            game.change_direction(key)
            
            # 恢复终端设置
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
            
            time.sleep(0.2)
    except:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
    
    print("\n游戏结束！")
    print(f"最终得分: {game.score}")

if __name__ == "__main__":
    # 根据平台选择运行方式
    import platform
    if platform.system() == "Windows":
        print("这是一个简化的贪吃蛇游戏，完整版本需要在支持键盘输入的终端中运行。")
        print("按 Enter 查看游戏说明...")
        input()
        
        # 显示说明
        game = SnakeGame()
        game.draw_board()
        print("游戏说明:")
        print("- 使用 w/a/s/d 控制蛇的方向 (上/左/下/右)")
        print("- 吃到 @ 符号可以增加分数")
        print("- 不要撞墙或撞到自己的身体")
        print("- 按 q 键退出游戏")
    else:
        simple_main()