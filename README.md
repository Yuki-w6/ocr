## Pixel
画像の最小単位。色と位置情報を含む。

```python
img = cv2.imread(path)
pixel = img[y, x]
```

#### Imread()
プログラム内で画像を扱うための関数。
#### Imshow
画像を表示するためのコマンド。

## 範囲
```python
img = cv2.imread(path)
roi = img[y:y+h, x:x+w]
```

## トラブルシューティング
- qt.qpa.plugin: Could not find the Qt platform plugin "offscreen" in ~

QT_QPA_PLATFORMを指定することで解決。以下を実行した後に再度実行
```bash
export QT_QPA_PLATFORM=xcb
```