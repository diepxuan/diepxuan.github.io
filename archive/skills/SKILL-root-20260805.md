**Advanced Condition Monitoring System with Sub-agent Prioritization**

- Enhanced proactive monitoring approach that analyzes all sub-agents before spawning new ones
- Priority-based decision flow:
  1. Check active/recent subagents status using `subagents list`
  2. Evaluate completion markers in memory
  3. Prioritize based on timeout thresholds and progress reports
- Integrated with PR management system to:
  - Maintain single PR for continuous updates
  - Track crawling progress through Git diff checks
- Automated PR maintenance schedule:
  - Daily: Review 10% of crawled documents
  - Weekly: Metrics dashboard update
  - Monthly: Full repository audit

**Skill Description:**
This skill formalizes the enhanced monitoring system that integrates sub-agent status checks with PR management for efficient legislative document crawling.

**Priority:** High
**Requirements:**
- Must maintain single PR for ongoing tasks
- Weekly metrics monitoring
- Daily documentation reviews

**version** : sha256:6f5e8d1a3b9c7d2e4a0f9e1c6d8b6a8f