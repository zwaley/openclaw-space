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

def play_game():
    game = SnakeGame()
    
    print("欢迎来到贪吃蛇游戏！")
    print("规则说明：")
    print("- 使用 w(上)/a(左)/s(下)/d(右) 控制方向")
    print("- O 是蛇头，o 是蛇身，@ 是食物")
    print("- 吃到食物得分，撞墙或撞到自己则游戏结束")
    print("- 按 Enter 键开始游戏...")
    input()
    
    # 一个简化版本，每步需要用户输入
    while not game.game_over:
        game.draw_board()
        print(f"当前方向: {game.direction}, 当前分数: {game.score}")
        
        move_result = input("请输入移动指令(w/a/s/d)或q退出: ").strip().lower()
        
        if move_result == 'q':
            print("游戏提前结束！")
            break
        elif move_result in ['w', 'a', 's', 'd']:
            # 更新方向，防止反向移动
            if move_result == 'w' and game.direction != 'DOWN':
                game.direction = 'UP'
            elif move_result == 's' and game.direction != 'UP':
                game.direction = 'DOWN'
            elif move_result == 'a' and game.direction != 'RIGHT':
                game.direction = 'LEFT'
            elif move_result == 'd' and game.direction != 'LEFT':
                game.direction = 'RIGHT'
        
        # 移动蛇
        game.move_snake()
    
    print("\n游戏结束！")
    print(f"最终得分: {game.score}")
    print("感谢游玩！")

if __name__ == "__main__":
    play_game()