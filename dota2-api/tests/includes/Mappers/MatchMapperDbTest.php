<?php

use Dota2Api\Utils\Db;
use Dota2Api\Mappers\LeaguesMapperWeb;
use Dota2Api\Mappers\LeaguesMapperDb;
use Dota2Api\Mappers\MatchMapperDb;
use Dota2Api\Mappers\MatchMapperWeb;
use Dota2Api\Models\Player;

class MatchMapperDbTest extends PHPUnit_Framework_TestCase
{

    public $matchId = '683300315';

    public static function setUpBeforeClass()
    {
        $leaguesMapperWeb = new LeaguesMapperWeb();
        $leagues = $leaguesMapperWeb->load();
        $leaguesMapperDb = new LeaguesMapperDb();
        $leaguesMapperDb->save($leagues[600]);
    }

    public static function tearDownBeforeClass()
    {
        $db = Db::obtain();
        $db->exec('DELETE FROM picks_bans');
        $db->exec('DELETE FROM ability_upgrades');
        $db->exec('DELETE FROM additional_units');
        $db->exec('DELETE FROM slots');
        $db->exec('DELETE FROM matches');
        $db->exec('DELETE FROM leagues');
    }

    public function testLoad()
    {

        $expectedMatchInfo = array(
            'game_mode' => '2',
            'radiant_win' => '1',
            'first_blood_time' => '7',
            'leagueid' => '600',
            'duration' => '1662'
        );

        $mapperWeb = new MatchMapperWeb($this->matchId);
        $match = $mapperWeb->load();
        $mapperDb = new MatchMapperDb();
        $mapperDb->save($match);
        $match = $mapperDb->load($this->matchId);

        $this->assertInstanceOf('Dota2Api\Models\Match', $match);
        foreach ($expectedMatchInfo as $k => $v) {
            $this->assertEquals($v, $match->get($k));
        }
        $expectedSlotsInfo = array(
            0 => array(
                'ability_upgrades' => 13,
                'level' => 13
            ),
            1 => array(
                'ability_upgrades' => 16,
                'level' => 16
            ),
            2 => array(
                'ability_upgrades' => 15,
                'level' => 15
            ),
            3 => array(
                'ability_upgrades' => 17, // player got level up but didn't choose any spell
                'level' => 18
            ),
            4 => array(
                'ability_upgrades' => 14,
                'level' => 14
            ),
            128 => array(
                'ability_upgrades' => 11,
                'level' => 11
            ),
            129 => array(
                'ability_upgrades' => 16,
                'level' => 16
            ),
            130 => array(
                'ability_upgrades' => 13,
                'level' => 13
            ),
            131 => array(
                'ability_upgrades' => 13,
                'level' => 13
            ),
            132 => array(
                'ability_upgrades' => 11,
                'level' => 11
            )
        );
        $slots = $match->getAllSlots();
        foreach ($expectedSlotsInfo as $slotId => $slot) {
            $this->assertTrue($slots[$slotId]->get('account_id') !== Player::ANONYMOUS);
            $this->assertEquals($slot['level'], (int)$slots[$slotId]->get('level'));
            $this->assertEquals($slot['ability_upgrades'], count($slots[$slotId]->getAbilitiesUpgrade()));
        }

        $picksBans = $match->getAllPicksBans();
        $this->assertInternalType('array', $picksBans);
        $fl = true;
        foreach ($picksBans as $r) {
            if (!in_array($r['is_pick'], array('1', '0'), true)) {
                $fl = false;
            }
        }
        $this->assertTrue($fl);

    }

    public function testUpdate()
    {
        $mapperDb = new MatchMapperDb();
        $match = $mapperDb->load($this->matchId);
        $match->set('first_blood_time', 0);
        $slots = $match->getAllSlots();
        $slots[0]->set('hero_id', '1');
        $match->setAllSlots($slots);
        $mapperDb->update($match, false);

        $match = $mapperDb->load($this->matchId);

        $this->assertEquals(0, $match->get('first_blood_time'));
        $slots = $match->getAllSlots();
        $this->assertEquals(1, $slots[0]->get('hero_id'));

    }

    public function testDelete()
    {
        $mapperDb = new MatchMapperDb();
        $match = $mapperDb->load($this->matchId);
        $mapperDb->save($match);

        $mapperDb->delete($match->get('match_id'));

        $match = $mapperDb->load($this->matchId);
        $this->assertNull($match->get('match_id'));
    }

}
