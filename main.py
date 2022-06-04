import sys
import pygame
import random as rd

def RandomColor():
    R = rd.randrange(0, 255)
    G = rd.randrange(0, 255)
    B = rd.randrange(0, 255)
    return (R, G, B)

def main():
    # pygameの初期化
    pygame.init()
    # メイン画面（Surface）初期化(横, 縦)
    width = 300
    height = 300
    main_surface = pygame.display.set_mode((width, height))
    # メイン画面のタイトル
    pygame.display.set_caption("Pygame Sample")
    # フォントオブジェクト生成（引数：フォント名とフォントサイズ）
    # フォント名にNoneを指定するとPygameの既定のフォントになる
    font = pygame.font.Font(None, 30)
    # テキストのSurfaceオブジェクトの生成（引数：テキスト内容、antialias、文字の色RGB）
    text_surface = font.render("DVD", True, (0, 0, 255))
    # メイン画面の色設定（引数：RGB）
    main_surface.fill((220, 220, 220))
    # メイン画面上にテキストを配置（引数：配置するSurface、座標）
    x = rd.randrange(0, width)
    y = rd.randrange(0, height)
    main_surface.blit(text_surface, (x, y))
    # メイン画面の更新
    pygame.display.update()
    # Clockオブジェクトの生成
    clock = pygame.time.Clock()
    # 速度の初期値
    vx = 2
    vy = -2

    # ループを続けるかのフラグ
    going = True
    # 終了イベント発生までループをまわす
    while going:
        # イベントを取得
        for event in pygame.event.get():
            # 終了イベント（画面の×ボタン押下など）の場合、
            # ループを抜ける
            if event.type == pygame.QUIT:
                going = False

        # 画面初期化
        main_surface.fill((220, 220, 220))
        # 移動
        x += vx
        y += vy

        # 衝突判定
        if x < 0 or x > width:
            vx *= -1
            vx += rd.uniform(-1, 1)
            color = RandomColor()
            text_surface = font.render("DVD", True, color)
        if y < 0 or y > height:
            vy *= -1
            vy += rd.uniform(-1, 1)
            color = RandomColor()
            text_surface = font.render("DVD", True, color)

        # 描画
        main_surface.blit(text_surface, (x, y))
        # 更新
        pygame.display.update()

        # フレームレート（1秒間に何回画面を更新するか）の設定
        clock.tick(30)


    # 終了処理
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()