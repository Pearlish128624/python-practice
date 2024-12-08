import csv
import random
import os

def get_project_root():
    """获取项目根目录"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return current_dir

def test_csv_exists():
    """测试CSV文件是否存在并且可以正确读取"""
    try:
        project_root = get_project_root()
        csv_path = os.path.join(project_root, 'source', 'vocabulary.csv')
        
        print(f"\n=== Testing CSV File ===")
        print(f"Looking for CSV at: {csv_path}")
        
        print(f"Current directory: {project_root}")
        print(f"Expected CSV path: {csv_path}")
        
        if not os.path.exists(csv_path):
            print("❌ CSV file not found!")
            return False
            
        with open(csv_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            words = list(reader)
            
        print(f"✓ CSV file found and readable")
        print(f"✓ Total words: {len(words)}")
        
        # 测试数据格式
        if words:
            sample = words[0]
            print("\nSample word format:")
            for key, value in sample.items():
                print(f"{key}: {value}")
        
        return True
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

def test_flow_module():
    """测试flow.py模块是否可以正确导入和使用"""
    try:
        print("\n=== Testing Flow Module ===")
        print("Attempting to import flow module...")
        
        from flow import ReadQuestion
        print("✓ Successfully imported ReadQuestion")
        
        # 测试ReadQuestion函数
        print("\nTesting ReadQuestion function...")
        word, meaning = ReadQuestion()
        
        print(f"✓ Got word: {word}")
        print(f"✓ Got meaning: {meaning}")
        
        return True
        
    except ImportError as e:
        print(f"❌ Import Error: {str(e)}")
        return False
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

def main():
    """运行所有测试"""
    print("🚀 Starting Tests...")
    
    # 测试CSV文件
    csv_test_passed = test_csv_exists()
    
    # 只有在CSV测试通过后才测试flow模块
    if csv_test_passed:
        flow_test_passed = test_flow_module()
    else:
        print("\n⚠️ Skipping flow module test due to CSV test failure")
        flow_test_passed = False
    
    # 总结
    print("\n=== Test Summary ===")
    print(f"CSV Test: {'✓ Passed' if csv_test_passed else '❌ Failed'}")
    print(f"Flow Module Test: {'✓ Passed' if flow_test_passed else '❌ Failed'}")

if __name__ == "__main__":
    main() 