# 氣球防線：國王學院（Balloon Defense）

一個氣球塔防小遊戲，單一 HTML 檔，直接用瀏覽器打開 `index.html` 就能自己玩。

## 地圖
King's Christian College（Logan Village 校區）。校園邊界、Logan River、Anzac Avenue、
停車場、圓環和運動場都來自 OpenStreetMap（© OpenStreetMap 貢獻者，ODbL）。
中學大樓的位置是示意，OpenStreetMap 上還沒有校內建築資料。

## 玩法
- 20 個回合，起始 100 生命、650 金幣；氣球跑進中學大樓就扣生命
- 主角（英雄）：全場一位，打破氣球累積經驗自動升到 5 級，5 級解鎖「能量爆發」
- 4 種防禦塔，各可升級 2 次：飛鏢塔、炸彈塔、冰凍塔、狙擊塔
- 快捷鍵：`1`–`4` 選塔、`5` 主角、空白鍵開始回合、`Q` 能量爆發、`U` 升級、`S` 賣出、`Esc` 取消

## 和朋友一起玩
在 claude.ai 的分享連結裡打開時，可以建立房間（4 字房號），朋友輸入房號加入。
金幣和生命共用；房主的分頁負責運行遊戲。直接打開本機檔案時只有單人模式。

## 主角頭像
照片不放進這個公開 repo。要做有頭像的版本：

    python3 tools/build_with_avatar.py 你的頭像.jpg dist/index.html

沒有頭像時，主角會用畫出來的卡通臉。
