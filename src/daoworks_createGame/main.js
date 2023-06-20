// ゲーム画面の準備
const canvas = document.getElementById("gameCanvas");
const context = canvas.getContext("2d");

// ゲームオブジェクトの定義
const player = {
  x: 50,
  y: 50,
  width: 20,
  height: 20,
  speed: 5,
};

// ゲームループ
function gameLoop() {
  // ゲームの更新処理
  update();

  // ゲームの描画処理
  render();

  // 次のフレームの実行
  requestAnimationFrame(gameLoop);
}

// ゲームの更新処理
function update() {
  // プレイヤーの移動処理
  if (keys["ArrowUp"]) {
    player.y -= player.speed;
  }
  if (keys["ArrowDown"]) {
    player.y += player.speed;
  }
  if (keys["ArrowLeft"]) {
    player.x -= player.speed;
  }
  if (keys["ArrowRight"]) {
    player.x += player.speed;
  }
}

// ゲームの描画処理
function render() {
  // 画面をクリア
  context.clearRect(0, 0, canvas.width, canvas.height);

  // プレイヤーを描画
  context.fillStyle = "blue";
  context.fillRect(player.x, player.y, player.width, player.height);
}

// キーボードの状態を格納するオブジェクト
const keys = {};

// キーボードのキーが押されたときの処理
document.addEventListener("keydown", function (event) {
  keys[event.key] = true;
});

// キーボードのキーが離されたときの処理
document.addEventListener("keyup", function (event) {
  keys[event.key] = false;
});

// ゲームループの開始
gameLoop();
