// frontend/src/app/page.tsx
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
import { Activity, CheckCircle2, XCircle, Clock } from "lucide-react";

export default async function Home() {
  const res = await fetch('http://localhost:8000/logs', { cache: 'no-store' });
  const { data } = await res.json();

  return (
    <main className="p-8 bg-slate-50 min-h-screen">
      <div className="max-w-5xl mx-auto space-y-6">
        
        {/* 標題區 */}
        <div className="flex items-center gap-3">
          <Activity className="w-8 h-8 text-blue-600" />
          <h1 className="text-3xl font-bold tracking-tight">Urban-Pulse Dashboard</h1>
        </div>

        <Card>
          <CardHeader>
            <CardTitle>最近任務紀錄</CardTitle>
            <CardDescription>顯示最近 10 次 ETL 數據抓取的執行狀態</CardDescription>
          </CardHeader>
          <CardContent>
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead>任務名稱</TableHead>
                  <TableHead>城市</TableHead>
                  <TableHead>狀態</TableHead>
                  <TableHead>紀錄數量</TableHead>
                  <TableHead className="text-right">執行時間</TableHead>
                </TableRow>
              </TableHeader>
              <TableBody>
                {data.map((log: any) => (
                  <TableRow key={log._id}>
                    <TableCell className="font-medium text-blue-600">{log.task_name}</TableCell>
                    <TableCell>{log.city}</TableCell>
                    <TableCell>
                      {log.status === "success" ? (
                        <Badge variant="outline" className="text-green-600 border-green-200 bg-green-50 gap-1">
                          <CheckCircle2 className="w-3 h-3" /> Success
                        </Badge>
                      ) : (
                        <Badge variant="destructive" className="gap-1">
                          <XCircle className="w-3 h-3" /> Failed
                        </Badge>
                      )}
                    </TableCell>
                    <TableCell>{log.records_count} 筆</TableCell>
                    <TableCell className="text-right text-slate-500 flex items-center justify-end gap-1">
                      <Clock className="w-3 h-3" />
                      {new Date(log.created_at).toLocaleString()}
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