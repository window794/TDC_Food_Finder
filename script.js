/* ===== JS ===== */
import { DATA } from "./data.js";

const state = {
  q: "",
  author: "all",
  area: "all",
  restaurant: "all",
  coaster: "all",
  priceMin: null,
  priceMax: null,
  sort: "area,restaurant,menu",
};
const $ = (s) => document.querySelector(s);

function syncHeaderHeight() {
  // フレームの次のサイクルで実行して、DOM更新が完了してから高さを計算
  requestAnimationFrame(() => {
    const header = document.getElementById("pageHeader");
    const h = header.offsetHeight;
    document.documentElement.style.setProperty("--headH", h + "px");
  });
}
window.addEventListener("load", syncHeaderHeight);
window.addEventListener("resize", syncHeaderHeight);

const yen = (n) => `¥${Number(n).toLocaleString("ja-JP")}`;
const priceStr = (r) =>
  r.priceMin === r.priceMax
    ? yen(r.priceMin)
    : `${yen(r.priceMin)}〜${yen(r.priceMax)}`;

function initFilters() {
  // エリア
  const areas = ["すべて", ...new Set(DATA.map((r) => r.area))];
  $("#area").innerHTML = areas
    .map((a, i) => `<option value="${i ? a : "all"}">${a}</option>`)
    .join("");

  // 店舗
  const restaurants = [
    "すべて",
    ...Array.from(new Set(DATA.map((r) => r.restaurant))).sort((a, b) =>
      a.localeCompare(b, "ja")
    ),
  ];
  $("#restaurant").innerHTML = restaurants
    .map((x, i) => `<option value="${i ? x : "all"}">${x}</option>`)
    .join("");

  // コースター
  const coasters = [
    "すべて",
    ...Array.from(new Set(DATA.map((r) => r.coaster))).sort((a, b) =>
      a.localeCompare(b, "ja")
    ),
  ];
  $("#coaster").innerHTML = coasters
    .map((c, i) => `<option value="${i ? c : "all"}">${c}</option>`)
    .join("");

  // ▼ 考案者（ご指定の順番）
  const authorOrder = [
    "すべて",
    "伊沢拓司",
    "河村拓哉",
    "須貝駿貴",
    "鶴崎修功",
    "東言",
    "東問",
    "ふくらP",
    "山本祥彰",
  ];
  $("#author").innerHTML = authorOrder
    .map((name, i) => `<option value="${i ? name : "all"}">${name}</option>`)
    .join("");

  // プレースホルダと初期値
  $("#priceMin").placeholder = "価格min";
  $("#priceMax").placeholder = "価格max";
  $("#priceMin").value = "";
  $("#priceMax").value = "";
}

function getFiltered() {
  const q = (state.q || "").toLowerCase();
  return DATA.filter((r) => {
    if (state.area !== "all" && r.area !== state.area) return false;
    if (state.restaurant !== "all" && r.restaurant !== state.restaurant)
      return false;
    if (state.coaster !== "all" && r.coaster !== state.coaster) return false;
    if (state.author !== "all" && (r.author || "") !== state.author)
      return false;
    if (state.priceMin != null && r.priceMax < state.priceMin) return false;
    if (state.priceMax != null && r.priceMin > state.priceMax) return false;
    if (
      q &&
      !`${r.area} ${r.menu} ${r.restaurant} ${r.coaster}`
        .toLowerCase()
        .includes(q)
    )
      return false;
    return true;
  }).sort(sortFn());
}

function sortFn() {
  const c = new Intl.Collator("ja-JP");
  return {
    "area,restaurant,menu": (a, b) =>
      c.compare(a.area, b.area) ||
      c.compare(a.restaurant, b.restaurant) ||
      c.compare(a.menu, b.menu),
    priceAsc: (a, b) => a.priceMin - b.priceMin,
    priceDesc: (a, b) => b.priceMin - a.priceMin,
    menu: (a, b) => c.compare(a.menu, b.menu),
    restaurant: (a, b) => c.compare(a.restaurant, b.restaurant),
  }[state.sort];
}

function render() {
  const rows = getFiltered();
  const tbody = $("#tbody");

  // 一時的に表示をクリアしてレイアウト計算をリセット
  tbody.style.display = "none";
  tbody.innerHTML = "";

  // 次のフレームで実際のコンテンツを描画
  requestAnimationFrame(() => {
    const toRow = (r) => `
      <tr>
        <td class="cell-area"    data-label="エリア">${r.area}</td>
        <td class="cell-menu">${r.menu}</td>
        <td class="cell-author"  data-label="考案者">${r.author || ""}</td>
        <td class="cell-shop"    data-label="店舗"><a href="${
          r.url
        }" target="_blank" rel="noopener">${r.restaurant}</a></td>
        <td class="cell-coaster" data-label="コースター"><span class="pill">${
          r.coaster
        }</span></td>
        <td class="cell-price"   data-label="価格">${priceStr(r)}</td>
      </tr>`;

    tbody.innerHTML = rows.map(toRow).join("");
    tbody.style.display = "";
    $("#meta").textContent = `表示 ${rows.length} / 全${DATA.length}件`;

    // レンダリング完了後にヘッダー高さを再計算
    syncHeaderHeight();
  });
}
function attach() {
  $("#q").addEventListener("input", (e) => {
    state.q = e.target.value;
    render();
  });
  $("#author").addEventListener("change", (e) => {
    state.author = e.target.value;
    render();
  });
  $("#area").addEventListener("change", (e) => {
    state.area = e.target.value;
    render();
  });
  $("#restaurant").addEventListener("change", (e) => {
    state.restaurant = e.target.value;
    render();
  });
  $("#coaster").addEventListener("change", (e) => {
    state.coaster = e.target.value;
    render();
  });
  $("#priceMin").addEventListener("input", (e) => {
    state.priceMin = e.target.value ? Number(e.target.value) : null;
    render();
  });
  $("#priceMax").addEventListener("input", (e) => {
    state.priceMax = e.target.value ? Number(e.target.value) : null;
    render();
  });
  $("#sort").addEventListener("change", (e) => {
    state.sort = e.target.value;
    render();
  });
  $("#exportShown").addEventListener("click", () => {
    const csv = toCSV(getFiltered());
    download("tdc_food.csv", csv);
  });
}

function toCSV(rows) {
  const header = [
    "エリア名",
    "メニュー名",
    "考案者",
    "店舗名",
    "店舗リンク",
    "コースター",
    "価格",
  ];
  const lines = [header.join(",")];
  for (const r of rows) {
    lines.push(
      [
        r.area,
        r.menu,
        r.author || "",
        r.restaurant,
        r.url,
        r.coaster,
        priceStr(r),
      ]
        .map(csvEscape)
        .join(",")
    );
  }
  return lines.join("\n");
}
function csvEscape(v) {
  const s = `${v ?? ""}`.replace(/"/g, '""');
  return /[",\n]/.test(s) ? `"${s}"` : s;
}
function download(name, text) {
  const a = document.createElement("a");
  a.href = URL.createObjectURL(new Blob([text], { type: "text/csv" }));
  a.download = name;
  a.click();
}

function setupFilterToggle() {
  const header = document.getElementById("pageHeader");
  const btn = document.getElementById("toggleFilters");

  const isMobile = matchMedia("(max-width:768px)").matches;
  if (isMobile) {
    header.classList.add("collapsed");
    btn.textContent = "🔎 フィルタを表示";
    btn.setAttribute("aria-expanded", "false");
    // フィルタ開閉後にヘッダー高さを再計算
    setTimeout(syncHeaderHeight, 0);
  } else {
    btn.textContent = "🔎 フィルタを隠す";
    btn.setAttribute("aria-expanded", "true");
  }

  btn.addEventListener("click", () => {
    header.classList.toggle("collapsed");
    const collapsed = header.classList.contains("collapsed");
    btn.textContent = collapsed ? "🔎 フィルタを表示" : "🔎 フィルタを隠す";
    btn.setAttribute("aria-expanded", String(!collapsed));
    // アニメーション完了後にヘッダー高さを再計算
    setTimeout(syncHeaderHeight, 50);
  });

  matchMedia("(max-width:768px)").addEventListener("change", (e) => {
    if (!e.matches) {
      header.classList.remove("collapsed");
      btn.textContent = "🔎 フィルタを隠す";
      btn.setAttribute("aria-expanded", "true");
      setTimeout(syncHeaderHeight, 0);
    }
  });
}

/* 初期化 */
document.addEventListener("DOMContentLoaded", function () {
  initFilters();
  attach();
  render();
  syncHeaderHeight();
  setupFilterToggle();
});
