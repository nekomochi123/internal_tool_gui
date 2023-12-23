import os,sys
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import pandas as pd
    
def dir_path_select(iDir):
    defect_dir = filedialog.askdirectory(initialdir = iDir)
    entry_1.set(defect_dir)

def files_path_select(iDir):
    fTyp = [("", "*.csv")]
    recipe_file = filedialog.askopenfilename(filetypes=fTyp, initialdir=iDir)
    entry_2.set(recipe_file)
        
def calculation():
    # entryからそれぞれのパスを取得
    dir_path = entry_1.get()
    setting_path = entry_2.get()
    # プルダウンメニューから値を取得
    position_index = variable.get()
    messagebox.showinfo("ディレクトリパス", f"ディレクトリパスは{dir_path}\nファイルパスは{setting_path}\nプルダウンメニューの値は{position_index}")
    # 設定CSVファイルをデータフレームで読み込み
    df_setting_recipe = pd.read_csv(setting_path)
    # サブウィンドウの設定
    setting_window = Toplevel()
    setting_window.title("setting")
    tree = ttk.Treeview(setting_window)
    tree.column('#0',width=0, stretch='no')
    tree.pack()
    # DataFrameの各列をTreeviewの列として設定
    tree["columns"] = list(df_setting_recipe.columns)
  
    # DataFrameの各行をTreeviewに追加
    for index, row in df_setting_recipe.iterrows():
        tree.insert("", "end", values=list(row))
    
def dir_disp(*args):
    #　ディレクトリパスの文字列を取得
    dir_path = entry_1.get()
    #　ファイル名だけを抜き出し
    dir_path_name = os.path.basename(dir_path)
    #　ファイル名を表示
    dir_path_label["text"] = dir_path_name
   
# カレントディレクトリのパス取得用(実行ファイル対策)
try:
    iDir = os.path.abspath(os.path.dirname(sys.argv[0]))
except:
    iDir= os.path.abspath(os.path.dirname(__file__))

if __name__ == "__main__":
    root = Tk()
    root.title("GUIツール")
    
    # Frame1の作成
    frame_1 = ttk.Frame(root, padding=10)
    frame_1.grid(row=0, column=1, sticky=E)

    # フォルダ参照」ラベルの作成
    defect_Label = ttk.Label(frame_1, text="フォルダ参照 ", padding=(5, 2))
    defect_Label.pack(side=LEFT)

    #「フォルダ参照」エントリーの作成
    entry_1 = StringVar()
    defect_Entry = ttk.Entry(frame_1, textvariable=entry_1, width=30)
    defect_Entry.pack(side=LEFT)

    # 「フォルダ参照」ボタンの作成
    defect_Button = ttk.Button(frame_1, text="フォルダ参照", command=lambda:dir_path_select(iDir))
    defect_Button.pack(side=LEFT)

    # Frame2の作成
    frame_2 = ttk.Frame(root, padding=10)
    frame_2.grid(row=2, column=1, sticky=E)

    # 「ファイル参照」ラベルの作成
    recipe_Label = ttk.Label(frame_2, text="レシピ参照 ", padding=(5, 2))
    recipe_Label.pack(side=LEFT)

    # 「ファイル参照」エントリーの作成
    entry_2 = StringVar()
    recipe_Entry = ttk.Entry(frame_2, textvariable=entry_2, width=30)
    recipe_Entry.pack(side=LEFT)

    # 「ファイル参照」ボタンの作成
    recipe_Button = ttk.Button(frame_2, text="レシピ参照", command=lambda:files_path_select(iDir))
    recipe_Button.pack(side=LEFT)

    # Frame3の作成
    frame_3 = ttk.Frame(root, padding=10)
    frame_3.grid(row=4,column=1,sticky=W)

    # ドロップダウンリストの説明
    tray_position_Label = ttk.Label(frame_3, text="指定位置", padding=(5, 2))
    tray_position_Label.pack(side=LEFT)

    # ドロップダウンリストの作成
    option = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
    variable = IntVar()
    tray_position_Combo = ttk.Combobox (frame_3, width= 3, values = option, textvariable = variable )
    tray_position_Combo.pack(side=LEFT)

    # Frame4の作成
    frame_4 = ttk.Frame(root, padding=10)
    frame_4.grid(row=5,column=1,sticky=W)
    entry_1.trace('w', dir_disp)
    dir_Label = ttk.Label(frame_4, text="右に選択フォルダが表示されます。", padding=(5, 2))
    dir_Label.pack(side=LEFT)
    dir_path_label = ttk.Label(frame_4, text="", padding=(5, 2))
    dir_path_label.pack(side=LEFT)

    # 実行ボタンの設置
    execution_Button1 = ttk.Button(frame_3, text="実行", command=calculation)
    execution_Button1.pack(fill = "x", padx=30, side = "left")

root.mainloop()