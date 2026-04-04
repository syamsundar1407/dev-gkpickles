import gspread
import pandas as pd

def analyze_sheet():
    try:
        # Authenticate using the service account key you provided
        print("Authenticating with Google Cloud...")
        gc = gspread.service_account(filename='sandbox-443817-35c53c592bc4.json')
        
        # Open the Google Sheet by its ID from your URL
        sheet_id = '1JUHzc_L0TYlTwSPnC7gYPKopNc-uVjiWl60dTOdfsc0'
        print(f"Opening Google Sheet: {sheet_id}")
        sh = gc.open_by_key(sheet_id)
        
        # Select the specific worksheet by its gid
        worksheet = sh.get_worksheet_by_id(695715523)
        
        # Fetch all records into a pandas DataFrame
        print("Fetching data...")
        records = worksheet.get_all_records()
        df = pd.DataFrame(records)
        
        if df.empty:
            print("The sheet is empty or could not map headers.")
            return

        print("\n" + "="*40)
        print("📊 GOOGLE SHEET DATA ANALYSIS")
        print("="*40)
        
        print("\n📋 FIRST 5 ROWS:")
        print(df.head())
        
        print("\n📈 DATA OVERVIEW:")
        print(df.info())
        
        if 'Category' in df.columns:
            print("\n🌶️ CATEGORY BREAKDOWN:")
            print(df['Category'].value_counts().to_string())
            
        if 'Stock Status' in df.columns:
            print("\n📦 STOCK STATUS BREAKDOWN:")
            print(df['Stock Status'].value_counts().to_string())

        if 'Bestseller' in df.columns:
            print("\n🔥 BESTSELLERS:")
            print(df['Bestseller'].value_counts().to_string())
            
        print("\n✅ Analysis Complete!")
        
    except Exception as e:
        print(f"\n❌ Error analyzing sheet: {e}")
        print("Please ensure the Service Account email ('gkpickles@sandbox-443817.iam.gserviceaccount.com') has 'Viewer' or 'Editor' sharing access directly on the Google Sheet!")

if __name__ == "__main__":
    analyze_sheet()
