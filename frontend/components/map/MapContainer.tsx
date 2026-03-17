"use client"

import React from 'react'
import DeckGL from '@deck.gl/react'
import { Map } from 'react-map-gl/maplibre'
import 'maplibre-gl/dist/maplibre-gl.css'

// 設定初始視角 (台北車站附近)
const INITIAL_VIEW_STATE = {
  longitude: 121.517,
  latitude: 25.047,
  zoom: 12,
  pitch: 0,
  bearing: 0
}

export default function MapContainer() {
  // 從環境變數抓取 Key
  const MAPTILER_KEY = process.env.NEXT_PUBLIC_MAPTILER_KEY;
  // 使用 MapTiler 提供的基礎向量底圖樣式
  const mapStyle = `https://api.maptiler.com/maps/streets-v2/style.json?key=${MAPTILER_KEY}`;

  return (
    <div className="relative w-full h-full rounded-xl overflow-hidden shadow-inner border">
      <DeckGL
        initialViewState={INITIAL_VIEW_STATE}
        controller={true} // 讓 Deck.gl 處理縮放與平移
      >
        <Map 
          mapStyle={mapStyle} 
          reuseMaps // 優化效能
        />
      </DeckGL>
    </div>
  );
}