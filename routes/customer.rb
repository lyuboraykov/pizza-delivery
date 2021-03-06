pizzas_hash = {
    "pizzas": {
        "медитеранео": {
            "id": 1,
          "image": "https://www.dominos.bg/gallery/fmobile/1314medium.png",
            "products": ["доматен сос", "краве сирене", "моцарела", "пресни зелени чушки", "черни маслини", "пресни домати"]
        },
        "алфредо": {
            "id": 2,
          "image": "https://www.dominos.bg/gallery/fmobile/1352medium.png",
          "products": ["сметана", "моцарела", "пиле", "бейби спанак"]
        },
        "вита": {
            "id": 3,
          "image": "https://www.dominos.bg/gallery/fmobile/1351medium.png",
          "products": ["доматен сос", "моцарела", "краве сирене", "пресни домати", "бейби спанак"]
        },
        "маргарита": {
            "id": 4,
          "image": "https://www.dominos.bg/gallery/fmobile/1265medium.png",
          "products": ["доматен сос", "моцарела", "допълнително моцарела"]
        },
        "чикенита": {
            "id": 5,
          "image": "https://www.dominos.bg/gallery/fmobile/1341medium.png",
          "products": ["доматен сос", "моцарела", "пилешко филе", "пеперони", "домати", "ементал"]
        },
        "чик-чи-рик": {
            "id": 6,
          "image": "https://www.dominos.bg/gallery/fmobile/1290medium.png",
          "products": ["доматен сос", "моцарела", "крехко пиле", "топено сирене", "царевица"]
        }
    }
}

get '/customer' do
  pizzas = RpcCaller::call_method :getAvailablePizzas, nil
  erb :customer, locals: { pizzas: pizzas }
end