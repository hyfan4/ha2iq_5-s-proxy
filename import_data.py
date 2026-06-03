import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# 1. 引用你的私鑰金鑰檔案
cred = credentials.Certificate('firebase-key.json')

# 2. 初始化 Firebase，請替換成你自己的 Realtime Database 網址
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://ha2iq5-default-rtdb.firebaseio.com/'
})

# 3. 定義要導入的初始資料（嚴格對應你的草圖欄位）
initial_orders = {
    "order_001": {
        "product_name": "生寫真套組A",
        "character": "官俊臣",
        "receiver": "楊涵博",
        "original_price": 120,
        "purchase_price": 540,
        "payment_status": "已匯款",
        "logistics_status": "待發貨",
        "remarks": "首批預購，需補國內運費"
    },
    "order_002": {
        "product_name": "官方周邊徽章",
        "character": "左奇函",
        "receiver": "張奕然",
        "original_price": 85,
        "purchase_price": 380,
        "payment_status": "無卡存款",
        "logistics_status": "時代峰峻發貨",
        "remarks": "第二批"
    },
    "order_003": {
        "product_name": "個人PB寫真",
        "character": "張桂源",
        "receiver": "魏子宸",
        "original_price": 210,
        "purchase_price": 950,
        "payment_status": "未付款",
        "logistics_status": "數碼集運發貨",
        "remarks": "無"
    }
}

# 4. 寫入到資料庫的 'orders' 節點下
ref = db.reference('orders')
ref.set(initial_orders)

print("🎉 資料已成功導入 Firebase Realtime Database！")
