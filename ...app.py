import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="AURA WAR",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

HTML = r"""
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
*{
    box-sizing:border-box;
}

html,body{
    margin:0;
    padding:0;
    background:#050814;
    color:white;
    font-family:Arial,Helvetica,sans-serif;
}

body{
    overflow-x:hidden;
}

#app{
    width:100%;
    max-width:1500px;
    margin:auto;
    padding:18px;
}

.top{
    text-align:center;
    margin-bottom:18px;
}

.logo{
    font-size:42px;
    font-weight:1000;
    letter-spacing:6px;
    background:linear-gradient(90deg,#45c8ff,#d76cff,#6ff5d0);
    -webkit-background-clip:text;
    color:transparent;
    text-shadow:0 0 30px rgba(80,180,255,.3);
}

.subtitle{
    color:#aebbd8;
    font-size:15px;
    margin-top:5px;
}

.panel{
    background:linear-gradient(145deg,#10172a,#080d1c);
    border:1px solid #273454;
    border-radius:20px;
    padding:20px;
    box-shadow:0 15px 45px rgba(0,0,0,.35);
    margin-bottom:18px;
}

.panel-title{
    font-size:22px;
    font-weight:900;
    margin-bottom:14px;
}

.mode-row{
    display:flex;
    gap:14px;
}

.mode-btn{
    flex:1;
    padding:18px;
    border-radius:16px;
    border:2px solid #293653;
    background:#0c1324;
    color:#cdd7ec;
    font-size:20px;
    font-weight:900;
    cursor:pointer;
    transition:.2s;
}

.mode-btn:hover{
    transform:translateY(-2px);
    border-color:#55bfff;
}

.mode-btn.active{
    border-color:#59d1ff;
    background:linear-gradient(145deg,#102c46,#172047);
    color:white;
    box-shadow:0 0 25px rgba(60,190,255,.22);
}

.names{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:14px;
}

.name-box label{
    display:block;
    font-weight:800;
    color:#9fb0d1;
    margin-bottom:7px;
}

.name-box input{
    width:100%;
    padding:14px;
    border-radius:12px;
    border:1px solid #334260;
    outline:none;
    background:#070c18;
    color:white;
    font-size:17px;
}

.name-box input:focus{
    border-color:#55caff;
}

.character-grid{
    display:grid;
    grid-template-columns:repeat(6,1fr);
    gap:12px;
}

.char-card{
    min-height:150px;
    padding:14px 8px;
    border-radius:17px;
    background:#0b1222;
    border:2px solid #27334f;
    cursor:pointer;
    text-align:center;
    transition:.2s;
    position:relative;
    overflow:hidden;
}

.char-card:hover{
    transform:translateY(-4px);
    border-color:#69d7ff;
}

.char-card.selected{
    border-color:#fff;
    box-shadow:0 0 22px var(--c);
    transform:translateY(-4px);
}

.char-icon{
    font-size:43px;
    margin-bottom:7px;
}

.char-name{
    font-weight:1000;
    font-size:16px;
}

.char-element{
    font-size:12px;
    color:#9daaca;
    margin-top:4px;
}

.selected-tag{
    position:absolute;
    top:7px;
    right:7px;
    font-size:10px;
    background:#fff;
    color:#111;
    border-radius:8px;
    padding:3px 5px;
    font-weight:900;
}

#battleWrap{
    position:relative;
    width:100%;
    border-radius:25px;
    padding:5px;
    background:linear-gradient(135deg,#3ddcff,#8b62ff,#ff5dbd,#3ddcff);
    box-shadow:
        0 0 45px rgba(70,180,255,.18),
        0 20px 70px rgba(0,0,0,.5);
}

#game{
    width:100%;
    height:720px;
    display:block;
    background:#060916;
    border-radius:20px;
}

#hud{
    position:absolute;
    top:18px;
    left:22px;
    right:22px;
    display:grid;
    grid-template-columns:1fr 120px 1fr;
    gap:15px;
    pointer-events:none;
}

.hudbox{
    background:rgba(5,9,22,.82);
    border:1px solid rgba(255,255,255,.12);
    border-radius:14px;
    padding:10px 13px;
    backdrop-filter:blur(8px);
}

.hudname{
    font-weight:1000;
    font-size:17px;
    white-space:nowrap;
    overflow:hidden;
    text-overflow:ellipsis;
}

.hudright{
    text-align:right;
}

.bar{
    height:12px;
    margin-top:6px;
    background:#161d30;
    border-radius:20px;
    overflow:hidden;
}

.hp{
    height:100%;
    width:100%;
    background:linear-gradient(90deg,#42e879,#8cffbb);
    transition:.15s;
}

.hp2{
    background:linear-gradient(90deg,#ff5576,#ff9baf);
    margin-left:auto;
}

.energy{
    height:7px;
    margin-top:4px;
    background:#151b2c;
    border-radius:20px;
    overflow:hidden;
}

.energy-fill{
    height:100%;
    width:0%;
    background:linear-gradient(90deg,#54caff,#d77cff);
}

.timer{
    display:flex;
    justify-content:center;
    align-items:center;
    font-size:30px;
    font-weight:1000;
}

#countdown{
    position:absolute;
    inset:0;
    display:flex;
    justify-content:center;
    align-items:center;
    font-size:110px;
    font-weight:1000;
    color:white;
    text-shadow:
        0 0 10px #56d8ff,
        0 0 35px #7b68ff,
        0 0 70px #ff58ca;
    pointer-events:none;
    z-index:20;
}

.hidden{
    display:none !important;
}

#startOverlay{
    position:absolute;
    inset:0;
    border-radius:20px;
    display:flex;
    flex-direction:column;
    justify-content:center;
    align-items:center;
    background:rgba(3,7,18,.68);
    backdrop-filter:blur(5px);
    z-index:10;
}

.start-title{
    font-size:52px;
    font-weight:1000;
    letter-spacing:4px;
}

.start-sub{
    color:#c1cce0;
    margin:8px 0 20px;
    font-size:17px;
}

.start-btn{
    border:0;
    padding:16px 35px;
    border-radius:14px;
    color:white;
    font-size:20px;
    font-weight:1000;
    cursor:pointer;
    background:linear-gradient(90deg,#247dff,#a94cff);
    box-shadow:0 0 30px rgba(80,130,255,.35);
}

.start-btn:hover{
    transform:scale(1.04);
}

#result{
    position:absolute;
    inset:0;
    display:flex;
    justify-content:center;
    align-items:center;
    pointer-events:none;
    z-index:25;
}

.result-box{
    min-width:420px;
    max-width:80%;
    text-align:center;
    padding:35px 50px;
    border-radius:25px;
    background:rgba(5,8,20,.92);
    border:2px solid rgba(255,255,255,.2);
    box-shadow:0 0 70px rgba(100,120,255,.35);
}

.result-title{
    font-size:45px;
    font-weight:1000;
}

.result-sub{
    margin-top:8px;
    color:#bdc8dc;
    font-size:18px;
}

.restart-btn{
    pointer-events:auto;
    margin-top:22px;
    padding:13px 25px;
    border:none;
    border-radius:12px;
    background:#fff;
    color:#111;
    font-weight:1000;
    cursor:pointer;
}

.guide{
    background:linear-gradient(145deg,#10182b,#080d1b);
    border:1px solid #30405f;
    border-radius:22px;
    padding:25px;
    box-shadow:0 15px 40px rgba(0,0,0,.28);
}

.guide-title{
    text-align:center;
    font-size:30px;
    font-weight:1000;
    margin-bottom:20px;
}

.guide-grid{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:18px;
}

.guide-card{
    border-radius:17px;
    padding:20px;
    background:#080e1d;
    border:1px solid #273754;
}

.guide-card h3{
    margin:0 0 13px;
    font-size:21px;
}

.guide-line{
    font-size:17px;
    line-height:1.7;
    color:#d5def0;
}

.key{
    display:inline-block;
    padding:3px 8px;
    margin:2px;
    min-width:27px;
    text-align:center;
    border-radius:7px;
    background:#1a2540;
    border:1px solid #3a4c70;
    color:white;
    font-weight:900;
}

.tip{
    margin-top:18px;
    text-align:center;
    font-size:17px;
    color:#aebbd4;
    line-height:1.7;
}

#balloons{
    position:absolute;
    inset:0;
    pointer-events:none;
    overflow:hidden;
    z-index:30;
}

.balloon{
    position:absolute;
    bottom:-100px;
    font-size:42px;
    animation:rise 4.5s linear forwards;
}

@keyframes rise{
    0%{
        transform:translateY(0) rotate(0deg);
        opacity:1;
    }
    100%{
        transform:translateY(-850px) rotate(20deg);
        opacity:0;
    }
}

@media(max-width:1000px){
    .character-grid{
        grid-template-columns:repeat(3,1fr);
    }

    #game{
        height:620px;
    }
}

@media(max-width:700px){
    #app{
        padding:8px;
    }

    .logo{
        font-size:31px;
    }

    .names,
    .guide-grid{
        grid-template-columns:1fr;
    }

    .character-grid{
        grid-template-columns:repeat(2,1fr);
    }

    #game{
        height:520px;
    }

    #hud{
        grid-template-columns:1fr 70px 1fr;
        left:8px;
        right:8px;
        top:8px;
    }

    .hudname{
        font-size:12px;
    }

    .timer{
        font-size:22px;
    }

    #countdown{
        font-size:70px;
    }
}
</style>
</head>

<body>

<div id="app">

    <div class="top">
        <div class="logo">⚡ AURA WAR ⚡</div>
        <div class="subtitle">ANIME 1V1 ARENA · NO IMAGE · NO EXTERNAL ASSET</div>
    </div>

    <div class="panel">
        <div class="panel-title">🎮 CHỌN CHẾ ĐỘ</div>

        <div class="mode-row">
            <button id="mode1" class="mode-btn active">
                ⚔️ 1V1
            </button>

            <button id="modeCPU" class="mode-btn">
                🤖 VS MÁY
            </button>
        </div>
    </div>

    <div class="panel">
        <div class="panel-title">👤 NGƯỜI CHƠI</div>

        <div class="names">
            <div class="name-box">
                <label>⚡ Người chơi 1</label>
                <input id="name1" maxlength="20" value="Player 1">
            </div>

            <div class="name-box" id="name2Wrap">
                <label>🔥 Người chơi 2</label>
                <input id="name2" maxlength="20" value="Player 2">
            </div>
        </div>
    </div>

    <div class="panel">
        <div class="panel-title">⚔️ CHỌN NHÂN VẬT</div>

        <div id="characters1" class="character-grid"></div>

        <div id="characters2Title"
             style="font-size:18px;font-weight:900;margin:22px 0 12px;">
            👤 NHÂN VẬT P2
        </div>

        <div id="characters2" class="character-grid"></div>
    </div>

    <div id="battleWrap">

        <canvas id="game"></canvas>

        <div id="hud">

            <div class="hudbox">
                <div id="hudName1" class="hudname">PLAYER 1</div>

                <div class="bar">
                    <div id="hp1" class="hp"></div>
                </div>

                <div class="energy">
                    <div id="en1" class="energy-fill"></div>
                </div>
            </div>

            <div class="hudbox timer">
                <span id="time">60</span>
            </div>

            <div class="hudbox hudright">
                <div id="hudName2" class="hudname">PLAYER 2</div>

                <div class="bar">
                    <div id="hp2" class="hp hp2"></div>
                </div>

                <div class="energy">
                    <div id="en2" class="energy-fill"></div>
                </div>
            </div>

        </div>

        <div id="countdown" class="hidden">3</div>

        <div id="startOverlay">
            <div class="start-title">AURA WAR</div>
            <div class="start-sub">
                Chọn nhân vật rồi bước vào trận chiến.
            </div>
            <button id="startBtn" class="start-btn">
                ▶ BẮT ĐẦU TRẬN
            </button>
        </div>

        <div id="result" class="hidden">
            <div class="result-box">
                <div id="resultTitle" class="result-title"></div>
                <div id="resultSub" class="result-sub"></div>
                <button id="restartBtn" class="restart-btn">
                    ↻ ĐÁNH LẠI
                </button>
            </div>
        </div>

        <div id="balloons"></div>
    </div>

    <!-- HƯỚNG DẪN NẰM RIÊNG BÊN DƯỚI KHUNG ĐẤU -->
    <div class="guide">

        <div class="guide-title">
            📖 HƯỚNG DẪN CHƠI
        </div>

        <div class="guide-grid">

            <div class="guide-card">
                <h3>🔵 P1 — Người chơi 1</h3>

                <div class="guide-line">
                    <b>Di chuyển:</b>
                    <span class="key">A</span>
                    <span class="key">D</span>
                </div>

                <div class="guide-line">
                    <b>Nhảy:</b>
                    <span class="key">W</span>
                </div>

                <div class="guide-line">
                    <b>Rơi nhanh:</b>
                    <span class="key">S</span>
                </div>

                <div class="guide-line">
                    <b>Đánh thường:</b>
                    <span class="key">J</span>
                </div>

                <div class="guide-line">
                    <b>Skill:</b>
                    <span class="key">K</span>
                </div>

                <div class="guide-line">
                    <b>Dash:</b>
                    <span class="key">L</span>
                </div>

                <div class="guide-line">
                    <b>Heavy:</b>
                    <span class="key">U</span>
                </div>

                <div class="guide-line">
                    <b>Ultimate:</b>
                    <span class="key">I</span>
                </div>
            </div>

            <div class="guide-card">
                <h3>🔴 P2 — Người chơi 2</h3>

                <div class="guide-line">
                    <b>Di chuyển:</b>
                    <span class="key">←</span>
                    <span class="key">→</span>
                </div>

                <div class="guide-line">
                    <b>Nhảy:</b>
                    <span class="key">↑</span>
                </div>

                <div class="guide-line">
                    <b>Rơi nhanh:</b>
                    <span class="key">↓</span>
                </div>

                <div class="guide-line">
                    <b>Đánh thường:</b>
                    <span class="key">1</span>
                </div>

                <div class="guide-line">
                    <b>Skill:</b>
                    <span class="key">2</span>
                </div>

                <div class="guide-line">
                    <b>Dash:</b>
                    <span class="key">3</span>
                </div>

                <div class="guide-line">
                    <b>Heavy:</b>
                    <span class="key">4</span>
                </div>

                <div class="guide-line">
                    <b>Ultimate:</b>
                    <span class="key">5</span>
                </div>
            </div>

        </div>

        <div class="tip">
            ⚡ Năng lượng tự hồi <b>8 điểm/giây</b> ·
            🔥 Skill cần 25 năng lượng ·
            💥 Ultimate cần 100 năng lượng ·
            ⏱️ Trận đấu kéo dài tối đa <b>60 giây</b>.
            <br>
            ❤️ Hết HP hoặc hết thời gian sẽ quyết định người chiến thắng.
        </div>

    </div>

</div>

<script>
"use strict";

/* =========================================================
   CHARACTER DATA
========================================================= */

const CHARACTERS = {

    water:{
        name:"KAIRO",
        element:"THỦY",
        color:"#36c8ff",
        dark:"#1268a4",
        light:"#a7edff",
        accent:"#227aff",
        icon:"🌊",
        skillName:"THỦY LONG",
        ultimateName:"HẢI LONG DIỆT",
        style:"water"
    },

    fire:{
        name:"RENJI",
        element:"VIÊM",
        color:"#ff5638",
        dark:"#a92319",
        light:"#ffd09a",
        accent:"#ff9d24",
        icon:"🔥",
        skillName:"HỎA LƯU",
        ultimateName:"VIÊM LONG PHÁ",
        style:"fire"
    },

    thunder:{
        name:"RAI",
        element:"LÔI",
        color:"#ffe84b",
        dark:"#ad8610",
        light:"#fff9bd",
        accent:"#fff06a",
        icon:"⚡",
        skillName:"LÔI KÍCH",
        ultimateName:"THIÊN LÔI",
        style:"thunder"
    },

    flower:{
        name:"MIZUHA",
        element:"HOA",
        color:"#ff7ccf",
        dark:"#a82e78",
        light:"#ffd8f0",
        accent:"#ffb0e3",
        icon:"🌸",
        skillName:"HOA VŨ",
        ultimateName:"BÁCH HOA LOẠN VŨ",
        style:"flower"
    },

    rock:{
        name:"GARO",
        element:"ĐÁ",
        color:"#b8a98e",
        dark:"#635848",
        light:"#e2d7bd",
        accent:"#8e8068",
        icon:"🪨",
        skillName:"NHAM KÍCH",
        ultimateName:"ĐẠI ĐỊA CHẤN",
        style:"rock"
    },

    wind:{
        name:"KAZE",
        element:"GIÓ",
        color:"#6ff5d0",
        dark:"#218c78",
        light:"#d5fff4",
        accent:"#9bffe9",
        icon:"🌪️",
        skillName:"CUỒNG PHONG",
        ultimateName:"THIÊN PHONG LOẠN VŨ",
        style:"wind"
    }
};

const characterKeys = [
    "water",
    "fire",
    "thunder",
    "flower",
    "rock",
    "wind"
];

let selected1 = "water";
let selected2 = "fire";
let mode = "1v1";

/* =========================================================
   DOM
========================================================= */

const canvas = document.getElementById("game");
const ctx = canvas.getContext("2d");

const mode1Btn = document.getElementById("mode1");
const modeCPUBtn = document.getElementById("modeCPU");

const name1Input = document.getElementById("name1");
const name2Input = document.getElementById("name2");
const name2Wrap = document.getElementById("name2Wrap");

const chars1El = document.getElementById("characters1");
const chars2El = document.getElementById("characters2");
const chars2Title = document.getElementById("characters2Title");

const startOverlay = document.getElementById("startOverlay");
const startBtn = document.getElementById("startBtn");

const countdownEl = document.getElementById("countdown");

const resultEl = document.getElementById("result");
const resultTitle = document.getElementById("resultTitle");
const resultSub = document.getElementById("resultSub");
const restartBtn = document.getElementById("restartBtn");

const hp1El = document.getElementById("hp1");
const hp2El = document.getElementById("hp2");
const en1El = document.getElementById("en1");
const en2El = document.getElementById("en2");

const hudName1 = document.getElementById("hudName1");
const hudName2 = document.getElementById("hudName2");
const timeEl = document.getElementById("time");

let W = 1200;
let H = 720;

let floorY = 600;

function resizeCanvas(){

    const rect = canvas.getBoundingClientRect();

    W = Math.max(760, rect.width);
    H = Math.max(500, rect.height);

    const ratio = window.devicePixelRatio || 1;

    canvas.width = Math.floor(W * ratio);
    canvas.height = Math.floor(H * ratio);

    ctx.setTransform(ratio,0,0,ratio,0,0);

    floorY = H - 105;
}

window.addEventListener("resize",resizeCanvas);
resizeCanvas();

/* =========================================================
   AUDIO
========================================================= */

let audioCtx = null;
let masterGain = null;

function initAudio(){

    if(!audioCtx){

        audioCtx = new (
            window.AudioContext ||
            window.webkitAudioContext
        )();

        masterGain = audioCtx.createGain();
        masterGain.gain.value = .20;
        masterGain.connect(audioCtx.destination);
    }

    if(audioCtx.state === "suspended"){
        audioCtx.resume();
    }
}

function tone(
    freq,
    duration,
    type="sine",
    gain=.07,
    endFreq=null
){

    initAudio();

    const osc = audioCtx.createOscillator();
    const g = audioCtx.createGain();

    osc.type = type;

    osc.frequency.setValueAtTime(
        freq,
        audioCtx.currentTime
    );

    if(endFreq !== null){

        osc.frequency.exponentialRampToValueAtTime(
            Math.max(30,endFreq),
            audioCtx.currentTime + duration
        );
    }

    g.gain.setValueAtTime(
        .0001,
        audioCtx.currentTime
    );

    g.gain.exponentialRampToValueAtTime(
        gain,
        audioCtx.currentTime + .015
    );

    g.gain.exponentialRampToValueAtTime(
        .0001,
        audioCtx.currentTime + duration
    );

    osc.connect(g);
    g.connect(masterGain);

    osc.start();

    osc.stop(
        audioCtx.currentTime + duration + .03
    );
}

function noise(
    duration=.1,
    gain=.06,
    filterFreq=1800
){

    initAudio();

    const buffer = audioCtx.createBuffer(
        1,
        Math.floor(audioCtx.sampleRate * duration),
        audioCtx.sampleRate
    );

    const data = buffer.getChannelData(0);

    for(let i=0;i<data.length;i++){
        data[i] = Math.random()*2-1;
    }

    const source = audioCtx.createBufferSource();
    const filter = audioCtx.createBiquadFilter();
    const g = audioCtx.createGain();

    filter.type = "bandpass";
    filter.frequency.value = filterFreq;

    g.gain.setValueAtTime(
        gain,
        audioCtx.currentTime
    );

    g.gain.exponentialRampToValueAtTime(
        .0001,
        audioCtx.currentTime + duration
    );

    source.buffer = buffer;

    source.connect(filter);
    filter.connect(g);
    g.connect(masterGain);

    source.start();
}

function sfxSlash(){
    tone(450,.08,"sawtooth",.045,900);
    noise(.05,.025,2800);
}

function sfxHeavy(){
    tone(120,.18,"square",.08,50);
    noise(.14,.09,700);
}

function sfxHit(){
    noise(.08,.08,1000);
    tone(90,.09,"square",.045,40);
}

function sfxDash(style){

    if(style === "wind"){
        noise(.28,.07,3500);
        tone(500,.24,"sine",.035,1200);
    }else{
        noise(.14,.05,2400);
        tone(240,.14,"sawtooth",.03,750);
    }
}

function sfxSkill(style){

    if(style === "water"){
        tone(330,.3,"sine",.05,760);
        tone(540,.26,"sine",.04,1000);
    }

    else if(style === "fire"){
        noise(.25,.08,900);
        tone(180,.23,"sawtooth",.05,60);
    }

    else if(style === "thunder"){
        tone(900,.12,"square",.06,180);
        noise(.12,.06,4200);
    }

    else if(style === "flower"){
        tone(520,.3,"sine",.05,900);
        tone(780,.35,"sine",.035,1200);
    }

    else if(style === "rock"){
        tone(90,.3,"square",.08,40);
        noise(.25,.08,500);
    }

    else if(style === "wind"){
        noise(.45,.07,3800);
        tone(420,.4,"sine",.04,1250);
        tone(720,.3,"triangle",.025,1400);
    }
}

function sfxUltimate(style){

    tone(180,.28,"sine",.06,420);
    tone(360,.36,"sine",.05,900);

    setTimeout(()=>{

        noise(.42,.13,1100);
        tone(75,.4,"square",.1,35);

        if(style === "wind"){
            noise(.55,.09,4500);
            tone(900,.55,"sine",.04,1600);
        }

        if(style === "thunder"){
            tone(1100,.2,"square",.08,120);
            noise(.3,.09,5000);
        }

        if(style === "fire"){
            noise(.5,.12,800);
        }

        if(style === "water"){
            tone(300,.5,"sine",.06,950);
        }

        if(style === "rock"){
            tone(65,.55,"square",.12,30);
        }

        if(style === "flower"){
            tone(600,.5,"sine",.05,1300);
            tone(900,.45,"sine",.035,1600);
        }

    },260);
}

function sfxJump(){
    tone(280,.1,"sine",.03,620);
}

function sfxCountdown(n){

    if(n === 1){
        tone(880,.17,"square",.065,620);
    }else{
        tone(440,.17,"square",.06,320);
    }
}

function sfxFight(){

    tone(420,.16,"sawtooth",.075,900);
    tone(900,.3,"sine",.065,1500);
    noise(.1,.035,3000);
}

function sfxVictory(){

    tone(523,.18,"sine",.07,660);

    setTimeout(()=>{
        tone(659,.18,"sine",.07,830);
    },140);

    setTimeout(()=>{
        tone(784,.35,"sine",.09,1100);
    },280);
}

function sfxDefeat(){

    tone(320,.25,"sine",.06,220);

    setTimeout(()=>{
        tone(220,.4,"sine",.06,100);
    },180);
}

/* =========================================================
   INPUT
========================================================= */

const keys = {};

window.addEventListener("keydown",(e)=>{

    keys[e.key.toLowerCase()] = true;

    if([
        "arrowleft",
        "arrowright",
        "arrowup",
        "arrowdown",
        " "
    ].includes(e.key.toLowerCase())){
        e.preventDefault();
    }

    if(
        e.key === " " &&
        running &&
        !gameOver
    ){
        p1.attack();
    }
});

window.addEventListener("keyup",(e)=>{
    keys[e.key.toLowerCase()] = false;
});

/* =========================================================
   EFFECTS
========================================================= */

const particles = [];
const projectiles = [];
const rings = [];
const texts = [];

function particle(
    x,
    y,
    color,
    count=8,
    power=180
){

    for(let i=0;i<count;i++){

        const a = Math.random()*Math.PI*2;
        const s = Math.random()*power;

        particles.push({
            x:x,
            y:y,
            vx:Math.cos(a)*s,
            vy:Math.sin(a)*s,
            life:.35 + Math.random()*.45,
            max:.8,
            size:2+Math.random()*5,
            color:color
        });
    }
}

function ring(
    x,
    y,
    color,
    max=90
){

    rings.push({
        x:x,
        y:y,
        r:8,
        max:max,
        life:.45,
        color:color
    });
}

function floatingText(
    x,
    y,
    text,
    color="#fff"
){

    texts.push({
        x:x,
        y:y,
        text:text,
        color:color,
        life:.8,
        vy:-40
    });
}

/* =========================================================
   FIGHTER
========================================================= */

class Fighter{

    constructor(x,side,id,charKey,isCPU=false){

        this.x = x;
        this.y = floorY;

        this.vx = 0;
        this.vy = 0;

        this.side = side;
        this.id = id;

        this.charKey = charKey;
        this.char = CHARACTERS[charKey];

        this.isCPU = isCPU;

        this.hp = 100;
        this.energy = 0;

        this.width = 60;
        this.height = 112;

        this.grounded = true;

        this.facing = side === 1 ? 1 : -1;

        this.stun = 0;

        this.attackTimer = 0;
        this.attackCooldown = 0;
        this.attackHitDone = false;

        this.combo = 0;

        this.skillCooldown = 0;

        this.dashCooldown = 0;
        this.dashTimer = 0;

        this.heavyCooldown = 0;
        this.heavyTimer = 0;
        this.heavyHitDone = false;

        this.ultimateCooldown = 0;

        this.invincible = 0;

        this.hitFlash = 0;

        this.dead = false;

        this.cpuThink = 0;
        this.cpuMove = 0;
        this.cpuJumpTimer = 0;
    }

    get headY(){
        return this.y - this.height;
    }

    update(dt,enemy){

        if(this.dead) return;

        this.energy += 8 * dt;
        this.energy = Math.min(100,this.energy);

        this.attackCooldown =
            Math.max(0,this.attackCooldown-dt);

        this.skillCooldown =
            Math.max(0,this.skillCooldown-dt);

        this.dashCooldown =
            Math.max(0,this.dashCooldown-dt);

        this.heavyCooldown =
            Math.max(0,this.heavyCooldown-dt);

        this.ultimateCooldown =
            Math.max(0,this.ultimateCooldown-dt);

        this.invincible =
            Math.max(0,this.invincible-dt);

        this.hitFlash =
            Math.max(0,this.hitFlash-dt);

        this.stun =
            Math.max(0,this.stun-dt);

        if(this.attackTimer > 0){
            this.attackTimer -= dt;
        }

        if(this.heavyTimer > 0){
            this.heavyTimer -= dt;
        }

        if(this.dashTimer > 0){

            this.x += this.facing * 1200 * dt;

            particle(
                this.x,
                this.y-55,
                this.char.color,
                2,
                40
            );
        }

        else if(this.stun <= 0){

            if(this.isCPU){
                this.updateCPU(dt,enemy);
            }else{
                this.updatePlayer(dt);
            }
        }

        this.physics(dt);

        this.checkAttack(enemy);
    }

    updatePlayer(dt){

        let left = false;
        let right = false;
        let jump = false;
        let fastFall = false;

        if(this.id === 1){

            left = !!keys["a"];
            right = !!keys["d"];
            jump = !!keys["w"];
            fastFall = !!keys["s"];

            if(keys["j"]){
                this.attack();
                keys["j"] = false;
            }

            if(keys["k"]){
                this.skill();
                keys["k"] = false;
            }

            if(keys["l"]){
                this.dash();
                keys["l"] = false;
            }

            if(keys["u"]){
                this.heavy();
                keys["u"] = false;
            }

            if(keys["i"]){
                this.ultimate();
                keys["i"] = false;
            }
        }

        else{

            left = !!keys["arrowleft"];
            right = !!keys["arrowright"];
            jump = !!keys["arrowup"];
            fastFall = !!keys["arrowdown"];

            if(keys["1"]){
                this.attack();
                keys["1"] = false;
            }

            if(keys["2"]){
                this.skill();
                keys["2"] = false;
            }

            if(keys["3"]){
                this.dash();
                keys["3"] = false;
            }

            if(keys["4"]){
                this.heavy();
                keys["4"] = false;
            }

            if(keys["5"]){
                this.ultimate();
                keys["5"] = false;
            }
        }

        if(left){
            this.vx -= 1500*dt;
            this.facing = -1;
        }

        if(right){
            this.vx += 1500*dt;
            this.facing = 1;
        }

        if(!left && !right){
            this.vx *= Math.pow(.0001,dt);
        }

        this.vx = Math.max(-285,Math.min(285,this.vx));

        if(jump && this.grounded){
            this.jump();
        }

        if(fastFall && !this.grounded){
            this.vy += 1000*dt;
        }
    }

    updateCPU(dt,enemy){

        const dx = enemy.x - this.x;
        const dist = Math.abs(dx);

        this.cpuThink -= dt;

        if(this.cpuThink <= 0){

            this.cpuThink = .12 + Math.random()*.18;

            if(dist > 230){
                this.cpuMove = dx > 0 ? 1 : -1;
            }
            else if(dist < 110){
                this.cpuMove = Math.random() < .3
                    ? (dx > 0 ? -1 : 1)
                    : 0;
            }
            else{
                this.cpuMove = Math.random() < .5
                    ? (dx > 0 ? 1 : -1)
                    : 0;
            }

            if(
                Math.random() < .13 &&
                this.grounded
            ){
                this.jump();
            }

            if(
                Math.random() < .13 &&
                this.dashCooldown <= 0 &&
                dist > 150
            ){
                this.facing = dx >= 0 ? 1 : -1;
                this.dash();
            }

            if(
                dist < 125 &&
                Math.random() < .55
            ){
                this.attack();
            }

            if(
                dist < 300 &&
                this.energy >= 25 &&
                Math.random() < .24
            ){
                this.skill();
            }

            if(
                dist < 340 &&
                this.energy >= 100 &&
                Math.random() < .12
            ){
                this.ultimate();
            }

            if(
                dist < 160 &&
                Math.random() < .15
            ){
                this.heavy();
            }
        }

        if(this.cpuMove < 0){

            this.vx -= 1300*dt;
            this.facing = -1;
        }

        else if(this.cpuMove > 0){

            this.vx += 1300*dt;
            this.facing = 1;
        }

        else{

            this.vx *= Math.pow(.0001,dt);
        }

        this.vx = Math.max(-260,Math.min(260,this.vx));

        if(
            enemy &&
            Math.abs(enemy.x-this.x) < 300
        ){
            this.facing =
                enemy.x > this.x ? 1 : -1;
        }
    }

    physics(dt){

        if(this.dashTimer <= 0){

            this.vy += 1450*dt;

            this.x += this.vx*dt;
            this.y += this.vy*dt;
        }

        /*
         * QUAN TRỌNG:
         * KHÔNG có vertical knockback khi bị đánh.
         * y luôn được khóa trong arena.
         */

        if(this.y >= floorY){

            this.y = floorY;
            this.vy = 0;
            this.grounded = true;
        }
        else{

            this.grounded = false;
        }

        if(this.y < 20){

            this.y = 20;

            if(this.vy < 0){
                this.vy = 0;
            }
        }

        const margin = 45;

        if(this.x < margin){

            this.x = margin;

            if(this.vx < 0){
                this.vx = 0;
            }
        }

        if(this.x > W-margin){

            this.x = W-margin;

            if(this.vx > 0){
                this.vx = 0;
            }
        }

        this.vx = Math.max(
            -500,
            Math.min(500,this.vx)
        );

        this.vy = Math.max(
            -800,
            Math.min(1100,this.vy)
        );
    }

    jump(){

        if(!this.grounded) return;

        this.vy = -580;
        this.grounded = false;

        sfxJump();

        particle(
            this.x,
            this.y,
            this.char.light,
            8,
            100
        );
    }

    attack(){

        if(
            this.attackCooldown > 0 ||
            this.attackTimer > 0 ||
            this.stun > 0
        ){
            return;
        }

        this.attackTimer = .20;
        this.attackCooldown = .28;
        this.attackHitDone = false;

        this.combo++;

        if(this.combo > 3){
            this.combo = 1;
        }

        sfxSlash();

        particle(
            this.x + this.facing*50,
            this.y-65,
            this.char.color,
            5,
            120
        );
    }

    heavy(){

        if(
            this.heavyCooldown > 0 ||
            this.attackTimer > 0 ||
            this.stun > 0
        ){
            return;
        }

        this.heavyTimer = .30;
        this.heavyCooldown = .72;
        this.heavyHitDone = false;

        sfxHeavy();

        ring(
            this.x + this.facing*55,
            this.y-60,
            this.char.accent,
            90
        );
    }

    skill(){

        if(
            this.energy < 25 ||
            this.skillCooldown > 0 ||
            this.stun > 0
        ){
            return;
        }

        this.energy -= 25;
        this.skillCooldown = 1.0;

        const speed =
            this.charKey === "thunder" ? 850 :
            this.charKey === "wind" ? 780 :
            this.charKey === "fire" ? 650 :
            590;

        projectiles.push({

            owner:this,
            x:this.x + this.facing*60,
            y:this.y-62,

            vx:this.facing*speed,
            vy:0,

            life:2.0,

            damage:
                this.charKey === "rock" ? 18 :
                this.charKey === "thunder" ? 17 :
                this.charKey === "wind" ? 16 :
                15,

            style:this.char.style,
            size:
                this.charKey === "wind" ? 24 :
                18
        });

        sfxSkill(this.char.style);

        ring(
            this.x + this.facing*55,
            this.y-62,
            this.char.color,
            75
        );
    }

    dash(){

        if(
            this.dashCooldown > 0 ||
            this.stun > 0
        ){
            return;
        }

        this.dashCooldown = .70;
        this.dashTimer = .19;
        this.invincible = .19;

        sfxDash(this.char.style);

        ring(
            this.x,
            this.y-55,
            this.char.color,
            75
        );
    }

    ultimate(){

        if(
            this.energy < 100 ||
            this.ultimateCooldown > 0 ||
            this.stun > 0
        ){
            return;
        }

        this.energy = 0;
        this.ultimateCooldown = 4;

        sfxUltimate(this.char.style);

        ring(
            this.x,
            this.y-60,
            this.char.color,
            170
        );

        particle(
            this.x,
            this.y-60,
            this.char.light,
            35,
            280
        );

        const enemy =
            this.id === 1 ? p2 : p1;

        if(enemy){

            const dx = enemy.x-this.x;
            const dy = Math.abs(enemy.y-this.y);

            if(
                Math.abs(dx) <= 310 &&
                dy < 150 &&
                Math.sign(dx) === this.facing
            ){

                enemy.takeDamage(
                    32,
                    this
                );
            }
        }

        floatingText(
            this.x,
            this.y-150,
            this.char.ultimateName,
            this.char.color
        );
    }

    checkAttack(enemy){

        if(!enemy || enemy.dead) return;

        /*
         * ĐÁNH THƯỜNG
         */

        if(
            this.attackTimer > 0 &&
            !this.attackHitDone
        ){

            const reach =
                this.combo === 3 ? 120 : 105;

            const dx =
                enemy.x-this.x;

            const dy =
                Math.abs(
                    (enemy.y-55) -
                    (this.y-55)
                );

            if(
                Math.abs(dx) <= reach &&
                dy <= 85 &&
                Math.sign(dx) === this.facing
            ){

                const damage =
                    this.combo === 3 ? 9 : 7;

                enemy.takeDamage(
                    damage,
                    this
                );

                this.energy =
                    Math.min(
                        100,
                        this.energy+7
                    );

                this.attackHitDone = true;
            }
        }

        /*
         * HEAVY
         */

        if(
            this.heavyTimer > 0 &&
            !this.heavyHitDone
        ){

            const dx = enemy.x-this.x;

            const dy =
                Math.abs(
                    enemy.y-this.y
                );

            if(
                Math.abs(dx) <= 135 &&
                dy <= 90 &&
                Math.sign(dx) === this.facing
            ){

                enemy.takeDamage(
                    13,
                    this
                );

                this.energy =
                    Math.min(
                        100,
                        this.energy+10
                    );

                this.heavyHitDone = true;
            }
        }
    }

    takeDamage(damage,attacker){

        if(
            this.dead ||
            this.invincible > 0
        ){
            return;
        }

        this.hp -= damage;

        this.hp = Math.max(
            0,
            this.hp
        );

        this.hitFlash = .14;

        this.stun = .16;

        /*
         * FIX QUAN TRỌNG:
         * Chỉ knockback ngang.
         * Không đẩy vy lên.
         */

        const direction =
            attacker.x < this.x ? 1 : -1;

        this.vx =
            direction *
            Math.min(
                270,
                Math.max(
                    140,
                    180 + damage*4
                )
            );

        this.vy = Math.max(
            0,
            this.vy
        );

        /*
         * Nếu đang ở mặt đất,
         * tuyệt đối không tự nhảy.
         */

        if(this.y >= floorY){
            this.y = floorY;
            this.vy = 0;
            this.grounded = true;
        }

        sfxHit();

        particle(
            this.x,
            this.y-60,
            this.char.light,
            12,
            210
        );

        ring(
            this.x,
            this.y-60,
            "#ffffff",
            55
        );

        floatingText(
            this.x,
            this.y-100,
            "-" + damage,
            "#ffffff"
        );

        if(this.hp <= 0){

            this.dead = true;
            this.stun = 999;

            this.vx = 0;
            this.vy = 0;

            particle(
                this.x,
                this.y-60,
                this.char.color,
                28,
                260
            );
        }
    }

    draw(){

        const c = this.char;

        ctx.save();

        /*
         * shadow
         */

        ctx.globalAlpha = .28;

        ctx.fillStyle = "#000";

        ctx.beginPath();

        ctx.ellipse(
            this.x,
            floorY+4,
            50,
            10,
            0,
            0,
            Math.PI*2
        );

        ctx.fill();

        ctx.globalAlpha = 1;

        /*
         * dash afterimage
         */

        if(this.dashTimer > 0){

            for(let i=1;i<=4;i++){

                ctx.globalAlpha =
                    .16 - i*.025;

                this.drawBody(
                    this.x -
                    this.facing*i*25,
                    this.y,
                    true
                );
            }

            ctx.globalAlpha = 1;
        }

        this.drawBody(
            this.x,
            this.y,
            false
        );

        ctx.restore();
    }

    drawBody(x,y,ghost){

        const c = this.char;

        ctx.save();

        ctx.translate(x,y);

        if(this.facing < 0){
            ctx.scale(-1,1);
        }

        /*
         * aura
         */

        ctx.globalAlpha =
            ghost ? .35 : .22;

        const aura =
            ctx.createRadialGradient(
                0,-62,
                5,
                0,-62,
                70
            );

        aura.addColorStop(
            0,
            c.light
        );

        aura.addColorStop(
            1,
            "transparent"
        );

        ctx.fillStyle = aura;

        ctx.beginPath();

        ctx.arc(
            0,
            -62,
            70,
            0,
            Math.PI*2
        );

        ctx.fill();

        ctx.globalAlpha =
            ghost ? .35 : 1;

        /*
         * legs
         */

        ctx.strokeStyle = "#111827";
        ctx.lineWidth = 10;
        ctx.lineCap = "round";

        ctx.beginPath();
        ctx.moveTo(-13,-35);
        ctx.lineTo(-19,-5);
        ctx.moveTo(13,-35);
        ctx.lineTo(19,-5);
        ctx.stroke();

        /*
         * body robe
         */

        ctx.fillStyle = c.dark;

        ctx.beginPath();

        ctx.moveTo(-25,-100);
        ctx.lineTo(25,-100);
        ctx.lineTo(33,-30);
        ctx.lineTo(0,-18);
        ctx.lineTo(-33,-30);
        ctx.closePath();

        ctx.fill();

        /*
         * shirt highlight
         */

        ctx.fillStyle = c.color;

        ctx.beginPath();

        ctx.moveTo(-14,-96);
        ctx.lineTo(5,-93);
        ctx.lineTo(17,-33);
        ctx.lineTo(0,-25);
        ctx.lineTo(-10,-48);
        ctx.closePath();

        ctx.fill();

        /*
         * head
         */

        ctx.fillStyle = "#f2c7a5";

        ctx.beginPath();

        ctx.arc(
            0,
            -120,
            23,
            0,
            Math.PI*2
        );

        ctx.fill();

        /*
         * hair
         */

        ctx.fillStyle = c.color;

        ctx.beginPath();

        ctx.moveTo(-27,-123);

        if(c.style === "wind"){

            ctx.lineTo(-20,-151);
            ctx.lineTo(-5,-138);
            ctx.lineTo(4,-164);
            ctx.lineTo(13,-139);
            ctx.lineTo(32,-154);
            ctx.lineTo(22,-119);
            ctx.lineTo(-25,-111);
        }

        else if(c.style === "fire"){

            ctx.lineTo(-22,-151);
            ctx.lineTo(-7,-137);
            ctx.lineTo(0,-160);
            ctx.lineTo(10,-138);
            ctx.lineTo(25,-151);
            ctx.lineTo(22,-116);
            ctx.lineTo(-24,-113);
        }

        else if(c.style === "thunder"){

            ctx.lineTo(-24,-151);
            ctx.lineTo(-8,-138);
            ctx.lineTo(0,-158);
            ctx.lineTo(10,-139);
            ctx.lineTo(25,-150);
            ctx.lineTo(20,-113);
            ctx.lineTo(-24,-113);
        }

        else if(c.style === "flower"){

            ctx.lineTo(-25,-148);
            ctx.lineTo(-8,-137);
            ctx.lineTo(0,-154);
            ctx.lineTo(10,-137);
            ctx.lineTo(27,-148);
            ctx.lineTo(20,-114);
            ctx.lineTo(-22,-114);
        }

        else{

            ctx.lineTo(-24,-149);
            ctx.lineTo(-8,-137);
            ctx.lineTo(0,-158);
            ctx.lineTo(10,-137);
            ctx.lineTo(25,-149);
            ctx.lineTo(20,-114);
            ctx.lineTo(-23,-114);
        }

        ctx.closePath();
        ctx.fill();

        /*
         * eyes
         */

        ctx.fillStyle = "#111";

        ctx.fillRect(
            6,
            -124,
            5,
            4
        );

        /*
         * arm
         */

        ctx.strokeStyle = c.light;
        ctx.lineWidth = 9;

        ctx.beginPath();

        ctx.moveTo(
            18,
            -82
        );

        ctx.lineTo(
            43,
            -62
        );

        ctx.stroke();

        /*
         * sword
         */

        ctx.strokeStyle = "#dfe8ff";
        ctx.lineWidth = 6;

        ctx.beginPath();

        ctx.moveTo(
            40,
            -63
        );

        ctx.lineTo(
            78,
            -115
        );

        ctx.stroke();

        ctx.strokeStyle = c.accent;
        ctx.lineWidth = 3;

        ctx.beginPath();

        ctx.moveTo(
            43,
            -66
        );

        ctx.lineTo(
            81,
            -118
        );

        ctx.stroke();

        /*
         * wind special visual
         */

        if(c.style === "wind" && !ghost){

            ctx.globalAlpha = .6;

            ctx.strokeStyle = c.light;
            ctx.lineWidth = 3;

            for(let i=0;i<3;i++){

                ctx.beginPath();

                ctx.arc(
                    -3,
                    -75,
                    45+i*9,
                    -1.2,
                    .35
                );

                ctx.stroke();
            }
        }

        ctx.restore();

        ctx.globalAlpha = 1;
    }
}

/* =========================================================
   GAME STATE
========================================================= */

let p1 = null;
let p2 = null;

let running = false;
let gameOver = false;

let matchTime = 60;

let lastTime = performance.now();

function createPlayers(){

    const n1 =
        name1Input.value.trim() ||
        "Player 1";

    const n2 =
        mode === "cpu"
        ? "CPU"
        : (
            name2Input.value.trim() ||
            "Player 2"
        );

    hudName1.textContent = n1;
    hudName2.textContent = n2;

    p1 = new Fighter(
        W*.28,
        1,
        1,
        selected1,
        false
    );

    p2 = new Fighter(
        W*.72,
        -1,
        2,
        selected2,
        mode === "cpu"
    );
}

/* =========================================================
   PROJECTILES
========================================================= */

function updateProjectiles(dt){

    for(let i=projectiles.length-1;i>=0;i--){

        const p = projectiles[i];

        p.x += p.vx*dt;
        p.y += p.vy*dt;

        p.life -= dt;

        const enemy =
            p.owner.id === 1 ? p2 : p1;

        if(enemy && !enemy.dead){

            const dx =
                enemy.x-p.x;

            const dy =
                Math.abs(
                    (enemy.y-60)-p.y
                );

            if(
                Math.abs(dx)<45 &&
                dy<65
            ){

                enemy.takeDamage(
                    p.damage,
                    p.owner
                );

                p.owner.energy =
                    Math.min(
                        100,
                        p.owner.energy+8
                    );

                particle(
                    p.x,
                    p.y,
                    p.owner.char.color,
                    10,
                    180
                );

                projectiles.splice(i,1);

                continue;
            }
        }

        if(
            p.life<=0 ||
            p.x<-100 ||
            p.x>W+100
        ){

            projectiles.splice(i,1);
        }
    }
}

function drawProjectile(p){

    const c = CHARACTERS[p.owner.charKey];

    ctx.save();

    ctx.translate(p.x,p.y);

    const angle =
        Math.atan2(p.vy,p.vx);

    ctx.rotate(angle);

    if(p.style === "wind"){

        ctx.strokeStyle = c.light;
        ctx.lineWidth = 4;

        for(let i=0;i<3;i++){

            ctx.beginPath();

            ctx.arc(
                0,
                0,
                15+i*6,
                -.8,
                .8
            );

            ctx.stroke();
        }

        ctx.fillStyle = c.color;

        ctx.beginPath();

        ctx.moveTo(28,0);
        ctx.lineTo(-15,-10);
        ctx.lineTo(-5,0);
        ctx.lineTo(-15,10);
        ctx.closePath();

        ctx.fill();
    }

    else{

        ctx.shadowBlur = 20;
        ctx.shadowColor = c.color;

        ctx.fillStyle = c.color;

        ctx.beginPath();

        ctx.arc(
            0,
            0,
            p.size,
            0,
            Math.PI*2
        );

        ctx.fill();

        ctx.fillStyle = c.light;

        ctx.beginPath();

        ctx.arc(
            -5,
            -5,
            p.size*.42,
            0,
            Math.PI*2
        );

        ctx.fill();

        if(p.style === "thunder"){

            ctx.strokeStyle = "#fff";

            ctx.lineWidth = 3;

            ctx.beginPath();

            ctx.moveTo(8,-10);
            ctx.lineTo(-3,2);
            ctx.lineTo(8,2);
            ctx.lineTo(-6,16);

            ctx.stroke();
        }
    }

    ctx.restore();
}

/* =========================================================
   EFFECT UPDATE
========================================================= */

function updateEffects(dt){

    for(let i=particles.length-1;i>=0;i--){

        const p = particles[i];

        p.life -= dt;

        p.vy += 350*dt;

        p.x += p.vx*dt;
        p.y += p.vy*dt;

        if(p.life<=0){
            particles.splice(i,1);
        }
    }

    for(let i=rings.length-1;i>=0;i--){

        const r = rings[i];

        r.life -= dt;

        r.r +=
            (r.max-r.r)*dt*5;

        if(r.life<=0){
            rings.splice(i,1);
        }
    }

    for(let i=texts.length-1;i>=0;i--){

        const t = texts[i];

        t.life -= dt;
        t.y += t.vy*dt;

        if(t.life<=0){
            texts.splice(i,1);
        }
    }
}

function drawEffects(){

    for(const r of rings){

        ctx.save();

        ctx.globalAlpha =
            Math.max(0,r.life/.45);

        ctx.strokeStyle = r.color;
        ctx.lineWidth = 4;

        ctx.beginPath();

        ctx.arc(
            r.x,
            r.y,
            r.r,
            0,
            Math.PI*2
        );

        ctx.stroke();

        ctx.restore();
    }

    for(const p of particles){

        ctx.save();

        ctx.globalAlpha =
            Math.max(0,p.life/p.max);

        ctx.fillStyle = p.color;

        ctx.beginPath();

        ctx.arc(
            p.x,
            p.y,
            p.size,
            0,
            Math.PI*2
        );

        ctx.fill();

        ctx.restore();
    }

    for(const t of texts){

        ctx.save();

        ctx.globalAlpha =
            Math.max(0,t.life/.8);

        ctx.font =
            "900 18px Arial";

        ctx.textAlign = "center";

        ctx.fillStyle = t.color;

        ctx.fillText(
            t.text,
            t.x,
            t.y
        );

        ctx.restore();
    }
}

/* =========================================================
   BACKGROUND
========================================================= */

function drawBackground(){

    const grad =
        ctx.createLinearGradient(
            0,
            0,
            0,
            H
        );

    grad.addColorStop(
        0,
        "#080d20"
    );

    grad.addColorStop(
        .55,
        "#11172d"
    );

    grad.addColorStop(
        1,
        "#050810"
    );

    ctx.fillStyle = grad;

    ctx.fillRect(
        0,
        0,
        W,
        H
    );

    /*
     * moon
     */

    const moon =
        ctx.createRadialGradient(
            W*.5,
            150,
            5,
            W*.5,
            150,
            150
        );

    moon.addColorStop(
        0,
        "rgba(150,190,255,.22)"
    );

    moon.addColorStop(
        1,
        "transparent"
    );

    ctx.fillStyle = moon;

    ctx.fillRect(
        0,
        0,
        W,
        H
    );

    /*
     * stars
     */

    ctx.fillStyle =
        "rgba(255,255,255,.35)";

    for(let i=0;i<70;i++){

        const x =
            (i*193)%W;

        const y =
            (i*79)%(floorY-100);

        const r =
            1+(i%3)*.5;

        ctx.beginPath();

        ctx.arc(
            x,
            y,
            r,
            0,
            Math.PI*2
        );

        ctx.fill();
    }

    /*
     * distant pillars
     */

    ctx.fillStyle =
        "rgba(35,45,75,.6)";

    for(let i=0;i<12;i++){

        const x =
            i*(W/11);

        const h =
            80+(i%4)*35;

        ctx.fillRect(
            x,
            floorY-h,
            45,
            h
        );
    }

    /*
     * floor
     */

    const floorGrad =
        ctx.createLinearGradient(
            0,
            floorY,
            0,
            H
        );

    floorGrad.addColorStop(
        0,
        "#17233b"
    );

    floorGrad.addColorStop(
        1,
        "#070b15"
    );

    ctx.fillStyle = floorGrad;

    ctx.fillRect(
        0,
        floorY,
        W,
        H-floorY
    );

    ctx.strokeStyle =
        "rgba(90,190,255,.35)";

    ctx.lineWidth = 2;

    ctx.beginPath();

    ctx.moveTo(
        0,
        floorY
    );

    ctx.lineTo(
        W,
        floorY
    );

    ctx.stroke();

    /*
     * floor grid
     */

    ctx.strokeStyle =
        "rgba(100,150,220,.12)";

    ctx.lineWidth = 1;

    for(let x=0;x<W;x+=70){

        ctx.beginPath();

        ctx.moveTo(
            x,
            floorY
        );

        ctx.lineTo(
            x+90,
            H
        );

        ctx.stroke();
    }
}

/* =========================================================
   DRAW
========================================================= */

function draw(){

    drawBackground();

    if(p1) p1.draw();
    if(p2) p2.draw();

    for(const p of projectiles){
        drawProjectile(p);
    }

    drawEffects();
}

/* =========================================================
   HUD
========================================================= */

function updateHUD(){

    if(!p1 || !p2) return;

    hp1El.style.width =
        p1.hp + "%";

    hp2El.style.width =
        p2.hp + "%";

    en1El.style.width =
        p1.energy + "%";

    en2El.style.width =
        p2.energy + "%";

    timeEl.textContent =
        Math.max(
            0,
            Math.ceil(matchTime)
        );
}

/* =========================================================
   END GAME
========================================================= */

function createBalloons(){

    const colors = [
        "🎈",
        "🎈",
        "🎈",
        "🎈",
        "🎈"
    ];

    const container =
        document.getElementById("balloons");

    container.innerHTML = "";

    for(let i=0;i<24;i++){

        const b =
            document.createElement("div");

        b.className = "balloon";

        b.textContent =
            colors[
                Math.floor(
                    Math.random()*colors.length
                )
            ];

        b.style.left =
            Math.random()*100 + "%";

        b.style.animationDelay =
            Math.random()*1.8 + "s";

        b.style.fontSize =
            (30+Math.random()*25)+"px";

        container.appendChild(b);

        setTimeout(()=>{
            b.remove();
        },6500);
    }
}

function endGame(reason){

    if(gameOver) return;

    gameOver = true;
    running = false;

    let winner = null;
    let loser = null;

    if(
        p1.hp > p2.hp
    ){
        winner = p1;
        loser = p2;
    }

    else if(
        p2.hp > p1.hp
    ){
        winner = p2;
        loser = p1;
    }

    else{

        resultTitle.textContent =
            "🤝 HÒA!";

        resultSub.textContent =
            "Hai chiến binh có cùng lượng HP.";

        resultEl.classList.remove("hidden");

        sfxVictory();

        return;
    }

    resultTitle.textContent =
        "🏆 " +
        (
            winner.id === 1
            ? (name1Input.value.trim() || "Player 1")
            : (
                mode === "cpu"
                ? "CPU"
                : (name2Input.value.trim() || "Player 2")
            )
        ) +
        " CHIẾN THẮNG!";

    if(winner.id === 1){

        resultSub.textContent =
            "🎉 Chúc mừng! Bạn đã giành chiến thắng!";

        createBalloons();

        sfxVictory();
    }

    else{

        resultSub.textContent =
            "😢 Tiếc quá! Hãy thử lại trận tiếp theo.";

        sfxDefeat();
    }

    resultEl.classList.remove("hidden");
}

/* =========================================================
   COUNTDOWN
========================================================= */

function countdown(){

    countdownEl.classList.remove("hidden");

    const nums = [
        "3",
        "2",
        "1",
        "FIGHT!"
    ];

    let i = 0;

    countdownEl.textContent =
        nums[i];

    sfxCountdown(3);

    const interval =
        setInterval(()=>{

            i++;

            if(i >= nums.length){

                clearInterval(interval);

                sfxFight();

                setTimeout(()=>{

                    countdownEl.classList.add("hidden");

                    running = true;

                },500);

                return;
            }

            countdownEl.textContent =
                nums[i];

            if(nums[i] === "2"){
                sfxCountdown(2);
            }

            else if(nums[i] === "1"){
                sfxCountdown(1);
            }

        },650);
}

/* =========================================================
   START / RESET
========================================================= */

function startGame(){

    initAudio();

    createPlayers();

    projectiles.length = 0;
    particles.length = 0;
    rings.length = 0;
    texts.length = 0;

    matchTime = 60;

    gameOver = false;
    running = false;

    resultEl.classList.add("hidden");

    document.getElementById(
        "balloons"
    ).innerHTML = "";

    startOverlay.classList.add("hidden");

    resizeCanvas();

    createPlayers();

    countdown();
}

function resetGame(){

    running = false;
    gameOver = false;

    resultEl.classList.add("hidden");

    startOverlay.classList.remove("hidden");

    projectiles.length = 0;
    particles.length = 0;
    rings.length = 0;
    texts.length = 0;

    document.getElementById(
        "balloons"
    ).innerHTML = "";

    draw();
}

/* =========================================================
   MAIN LOOP
========================================================= */

function loop(now){

    const dt =
        Math.min(
            .033,
            (now-lastTime)/1000
        );

    lastTime = now;

    if(running && !gameOver){

        matchTime -= dt;

        if(matchTime <= 0){

            matchTime = 0;

            endGame("timeout");
        }

        else{

            p1.update(dt,p2);
            p2.update(dt,p1);

            updateProjectiles(dt);
            updateEffects(dt);

            if(
                p1.dead ||
                p2.dead
            ){
                endGame("ko");
            }
        }
    }

    else{

        updateEffects(dt);
    }

    updateHUD();
    draw();

    requestAnimationFrame(loop);
}

requestAnimationFrame(loop);

/* =========================================================
   CHARACTER SELECT UI
========================================================= */

function renderCharacterCards(){

    chars1El.innerHTML = "";
    chars2El.innerHTML = "";

    for(const key of characterKeys){

        const c = CHARACTERS[key];

        const card1 =
            document.createElement("div");

        card1.className =
            "char-card" +
            (
                selected1 === key
                ? " selected"
                : ""
            );

        card1.style.setProperty(
            "--c",
            c.color
        );

        card1.innerHTML = `
            ${
                selected1 === key
                ? '<div class="selected-tag">P1</div>'
                : ""
            }
            <div class="char-icon">${c.icon}</div>
            <div class="char-name">${c.name}</div>
            <div class="char-element">${c.element}</div>
        `;

        card1.onclick = ()=>{

            selected1 = key;

            renderCharacterCards();
        };

        chars1El.appendChild(card1);


        const card2 =
            document.createElement("div");

        card2.className =
            "char-card" +
            (
                selected2 === key
                ? " selected"
                : ""
            );

        card2.style.setProperty(
            "--c",
            c.color
        );

        card2.innerHTML = `
            ${
                selected2 === key
                ? '<div class="selected-tag">P2</div>'
                : ""
            }
            <div class="char-icon">${c.icon}</div>
            <div class="char-name">${c.name}</div>
            <div class="char-element">${c.element}</div>
        `;

        card2.onclick = ()=>{

            selected2 = key;

            renderCharacterCards();
        };

        chars2El.appendChild(card2);
    }
}

renderCharacterCards();

/* =========================================================
   MODE
========================================================= */

mode1Btn.onclick = ()=>{

    mode = "1v1";

    mode1Btn.classList.add("active");
    modeCPUBtn.classList.remove("active");

    name2Wrap.style.display = "block";
    chars2Title.style.display = "block";
    chars2El.style.display = "grid";

    name2Input.value =
        name2Input.value === "CPU"
        ? "Player 2"
        : name2Input.value;
};

modeCPUBtn.onclick = ()=>{

    mode = "cpu";

    modeCPUBtn.classList.add("active");
    mode1Btn.classList.remove("active");

    name2Wrap.style.display = "none";
    chars2Title.style.display = "none";
    chars2El.style.display = "none";
};

/* =========================================================
   BUTTONS
========================================================= */

startBtn.onclick = ()=>{
    startGame();
};

restartBtn.onclick = ()=>{
    startGame();
};

/* =========================================================
   INITIAL
========================================================= */

draw();

</script>

</body>
</html>
"""

components.html(
    HTML,
    height=1500,
    scrolling=True
)
