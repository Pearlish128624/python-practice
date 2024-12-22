from typing import List, Dict, Union, Tuple

# 計算學生加權平均分的程序
def calculate_weighted_average(scores: List[Union[float, None]]) -> float:
    # 將None值過濾掉，只保留實際的分数
    valid_scores = [score for score in scores if score is not None]
    
    if not valid_scores:
        return 0
    
    # 計算學生參加的課程數量
    num_classes = len(valid_scores)
    
    if num_classes == 1:
        # 如果只參加了一門課，直接返回該分數
        return valid_scores[0]
    elif num_classes == 2:
        # 如果參加了兩門課，給較高分數更多權重
        # 計算方式：(最高分*2 + 最低分) / 3
        return round((max(valid_scores) * 2 + min(valid_scores)) / 3, 1)
    else:  # num_classes == 3
        # 如果參加了三門課，給最高分配更多權重
        # 計算方式：(最高分*3 + 第二高分 + 最低分) / 5
        sorted_scores = sorted(valid_scores, reverse=True)
        return round((sorted_scores[0] * 3 + sorted_scores[1] + sorted_scores[2]) / 5, 1)

def process_scores(scores_file: str) -> None:
    students: Dict[str, float] = {}
    
    # 讀取並處理成績文件
    with open(scores_file, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                name, scores_str = line.strip().split(' ', 1)  # 只分割第一個空格
                # 處理分數字串，移除 [] 並分割
                scores_str = scores_str.strip('[]')
                # 將分數轉換為數字，'X'轉換為None
                scores = [float(score.strip()) if score.strip() != 'X' else None 
                         for score in scores_str.split(',')]
                avg = calculate_weighted_average(scores)
                students[name] = avg
            except Exception as e:
                print(f"處理行 '{line.strip()}' 時發生錯誤: {e}")
                continue
    
    ranked_students: List[Tuple[str, float]] = sorted(
        students.items(),
        key=lambda x: (-x[1], x[0])  # 按分數降序，姓名升序排列
    )
    # 將排名寫入ranking.txt
    with open('ranking.txt', 'w', encoding='utf-8') as file:
        for i, (name, avg) in enumerate(ranked_students, 1):
            file.write(f"{i}. [{name}, {int(avg) if avg.is_integer() else avg}]\n")

if __name__ == "__main__":
    process_scores('scores.txt')