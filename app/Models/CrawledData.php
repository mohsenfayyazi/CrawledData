<?php

namespace App\Models;

use Jenssegers\Mongodb\Eloquent\Model;

class CrawledData extends Model
{
   protected $connection = 'mongodb';
   protected $collection = 'TheCrawledData';

}
