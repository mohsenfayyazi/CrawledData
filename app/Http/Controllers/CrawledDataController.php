<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\CrawledData;
use Symfony\Component\Process\Process;
use Symfony\Component\Process\Exception\ProcessFailedException;

class CrawledDataController extends Controller
{
    public function index()
    {
        $process = new Process(['python', '/var/www/laravel/CrawelData/app/Python/CrawlData.py']);
        $process->run();
        if (!$process->isSuccessful()) {
            throw new ProcessFailedException($process);
        }
        $TheCrawledData = CrawledData::all();
        return view('welcome')->with('TheCrawledData', $TheCrawledData);
    }
}
