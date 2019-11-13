from pathlib import Path
import shutil


current = Path(__file__).parent

score_directory_path = current / 'score_data'
score_directory_insurance_path = current / 'dest_data'

shutil.copytree(score_directory_path, score_directory_insurance_path)

files_path = score_directory_path.glob('**/*.csv')

header = '氏名,メールアドレス,得点\n'

for file_path in files_path:
    print(file_path)
    with file_path.open('r') as f:
        read_datas = f.readlines()

    with file_path.open('w') as f:
        read_datas.insert(0, header)
        f.writelines(read_datas)
        print(read_datas)