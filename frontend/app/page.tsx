// frontend/app/page.tsx
import { 
  Card, 
  CardContent, 
  CardDescription, 
  CardHeader, 
  CardTitle 
} from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { 
  Table, 
  TableBody, 
  TableCell, 
  TableHead, 
  TableHeader, 
  TableRow 
} from "@/components/ui/table";
import { Activity, CheckCircle2, XCircle, Clock, MapIcon } from "lucide-react";
import MapContainer from "@/components/map/MapContainer";

export default async function Home() {
  let data = [];
  try {
    const res = await fetch('http://localhost:8000/logs', { cache: 'no-store' });
    if (res.ok) {
      const json = await res.json();
      data = json.data || [];
    }
  } catch (e) {
    console.error("Backend fetch failed:", e);
  }

  return (
    <main className="h-screen w-screen bg-slate-50 flex flex-col overflow-hidden">
      
      {/* 1. Header: 固定高度 */}
      <header className="h-14 border-b bg-white flex items-center px-6 shrink-0 shadow-sm z-10">
        <div className="flex items-center gap-2">
          <Activity className="w-5 h-5 text-blue-600" />
          <h1 className="text-lg font-bold tracking-tight text-slate-800">Urban-Pulse</h1>
          <Badge variant="secondary" className="ml-2 font-mono text-[10px]">v1.0-alpha</Badge>
        </div>
      </header>

      {/* 2. Content Area: 填滿剩餘空間 */}
      <div className="flex-1 p-4 flex gap-4 overflow-hidden">
        
        {/* 左側：地圖佔據主要視角 */}
        <Card className="flex-3 flex flex-col shadow-none border-slate-200 overflow-hidden">
          <CardHeader className="py-3 px-5 shrink-0 border-b bg-white">
            <div className="flex items-center justify-between">
              <div className="flex items-center gap-2">
                <MapIcon className="w-4 h-4 text-blue-500" />
                <CardTitle className="text-sm font-semibold">台北市公車路網空間預覽</CardTitle>
              </div>
              <Badge variant="outline" className="text-[10px]">Real-time Spatial Data</Badge>
            </div>
          </CardHeader>
          <CardContent className="flex-1 p-0 relative bg-slate-100">
            {/* 確保 MapContainer 撐滿容器 */}
            <MapContainer />
          </CardContent>
        </Card>

        {/* 右側：日誌清單 */}
        <Card className="flex-1 flex flex-col shadow-none border-slate-200 overflow-hidden max-w-100">
          <CardHeader className="py-3 px-5 shrink-0 border-b bg-white">
            <CardTitle className="text-sm font-semibold">數據任務日誌</CardTitle>
            <CardDescription className="text-[11px]">最近 10 次執行紀錄</CardDescription>
          </CardHeader>
          
          <CardContent className="flex-1 overflow-y-auto p-0 scrollbar-hide">
            <Table>
              <TableHeader className="sticky top-0 bg-slate-50 z-20">
                <TableRow className="hover:bg-transparent">
                  <TableHead className="text-[11px] h-8">任務</TableHead>
                  <TableHead className="text-[11px] h-8">狀態</TableHead>
                  <TableHead className="text-[11px] h-8 text-right">時間</TableHead>
                </TableRow>
              </TableHeader>
              <TableBody>
                {data.map((log: any) => (
                  <TableRow key={log._id} className="hover:bg-slate-50/80 transition-colors">
                    <TableCell className="py-2 text-xs font-medium text-slate-700">
                      {log.task_name}
                    </TableCell>
                    <TableCell className="py-2">
                      {log.status === "success" ? (
                        <div className="flex items-center text-green-600">
                          <CheckCircle2 className="w-3 h-3 mr-1" />
                          <span className="text-[10px]">成功</span>
                        </div>
                      ) : (
                        <div className="flex items-center text-red-500">
                          <XCircle className="w-3 h-3 mr-1" />
                          <span className="text-[10px]">失敗</span>
                        </div>
                      )}
                    </TableCell>
                    <TableCell className="py-2 text-right text-[10px] text-slate-400 font-mono">
                      {new Date(log.created_at).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
                    </TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </CardContent>
        </Card>

      </div>
    </main>
  );
}