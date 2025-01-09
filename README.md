# mypkg
- 千葉工業大学未来ロボティクス学科ロボットシステム学授業・課題用  
- ROS2のパッケージ
- このパッケージは、psutil ライブラリをインストールする必要があります。以下のコマンドを入力しインストールしてください
  ```shell
  pip install psutil
  ```
  [![test](https://github.com/KeiyoNakayama/robosys_2/actions/workflows/test.yml/badge.svg)](https://github.com/KeiyoNakayama/robosys_2/actions/workflows/test.yml)
## 使用環境
- ROS2 foxy
- Ubuntu 20.04

## check_cpu_stats概要
- 1秒ごとにパソコンのCPU統計情報をトピックに流します。
- 流されるCPU統計情報:
  - コンテキストスイッチの総数
  - 割り込みが発生した回数
  - ソフト割り込みが発生した回数
  - システムコールを発行した回数
  
## 実行例
端末1：
```shell
$ ros2 run mypkg check_cpu_stats
```
端末2：
```shell
$ ros2 topic echo /cpu_stats
data: 'Context Switches: 835957, Interrupts: 229203, Soft Interrupts: 695360, Syscalls: 0'
---
data: 'Context Switches: 836078, Interrupts: 229223, Soft Interrupts: 695415, Syscalls: 0'
---
data: 'Context Switches: 836231, Interrupts: 229250, Soft Interrupts: 695512, Syscalls: 0'
---
```

## listener_cpu_stats概要
- check_cpu_statsのテスト用

## 著作権・ライセンス
- このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。  
- © 2025 Keiyo Nakayama
## 作者
Keiyo Nakayama  
keiyou0206@gmail.com
