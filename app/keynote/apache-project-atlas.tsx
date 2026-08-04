"use client";

import { ArrowUpRightIcon } from "lucide-react";
import Image from "next/image";

import {
  type ApacheDomainKey,
  apacheDomains,
  apacheLandscapeProjects,
} from "./apache-ecosystem";
import styles from "./page.module.css";

export default function ApacheProjectAtlas({
  activeDomain,
  onDomainChange,
  stage = false,
}: {
  activeDomain: ApacheDomainKey;
  onDomainChange?: (domain: ApacheDomainKey) => void;
  stage?: boolean;
}) {
  const selectedProjects = apacheLandscapeProjects;

  return (
    <div
      className={`${styles.apacheAtlas} ${styles.deepDive}`}
      data-stage={stage ? "true" : undefined}
    >
      <div className={styles.apacheAtlasHeading}>
        <div>
          <strong>APACHE PROJECT ATLAS</strong>
          <span>Apache 项目领域与 Agentic Landscape 入选</span>
        </div>
        <dl>
          <div><dt>领域</dt><dd>7 个</dd></div>
          <div><dt>来源</dt><dd>Apache Projects Directory</dd></div>
          <div><dt>数量</dt><dd>同一项目可属于多个领域</dd></div>
          <div><dt>头部项目</dt><dd>主要 GitHub repo stars</dd></div>
        </dl>
      </div>

      <div className={styles.apacheAtlasBody}>
        <div
          className={styles.apacheDomainTabs}
          role="tablist"
          aria-label="Apache 技术领域"
        >
          {(Object.keys(apacheDomains) as ApacheDomainKey[]).map((key) => (
            <button
              key={key}
              type="button"
              role="tab"
              tabIndex={stage ? -1 : undefined}
              aria-selected={activeDomain === key}
              className={activeDomain === key ? styles.activeDomain : ""}
              onClick={() => onDomainChange?.(key)}
            >
              <strong>{apacheDomains[key].count}</strong>
              <span>{apacheDomains[key].label}</span>
            </button>
          ))}
        </div>

        <article className={styles.apacheDomainDetail} key={activeDomain}>
          <div className={styles.apacheDomainLead}>
            <div>
              <span>PROJECT RECORDS</span>
              <strong>{apacheDomains[activeDomain].count}</strong>
            </div>
            <div className={styles.apacheDomainName}>
              <h3>{apacheDomains[activeDomain].label}</h3>
              <div className={styles.apacheLabelCloud}>
                {apacheDomains[activeDomain].officialLabels.map((label) => (
                  <span key={label}>{label}</span>
                ))}
              </div>
            </div>
            <p className={styles.apacheDomainDefinition}>
              {apacheDomains[activeDomain].definition}
            </p>
          </div>

          <div className={styles.apacheHeadProjects}>
            <p>HEAD PROJECTS · GITHUB STARS SNAPSHOT</p>
            <div>
              {apacheDomains[activeDomain].heads.map(([name, stars]) => (
                <span key={name}>
                  <strong>{name}</strong>
                  <small>★ {stars}</small>
                </span>
              ))}
            </div>
          </div>

          <div className={styles.apacheLandscapeMatch}>
            <p>6 APACHE PROJECTS IN AGENTIC LANDSCAPE</p>
            <div>
              {selectedProjects.map((project) => (
                <span key={project.name}>
                  <Image
                    src={project.logo}
                    alt=""
                    width={18}
                    height={18}
                  />
                  Apache {project.name}
                </span>
              ))}
            </div>
          </div>
        </article>
      </div>

      <div className={styles.apacheMetadataGap}>
        <strong>45</strong>
        <div>
          <span>目录中缺少可用项目分类的记录</span>
          <p>
            Paimon、Gravitino、Fory、Celeborn 等项目仍计入项目总览，但不参与上方领域数量统计。
          </p>
        </div>
        <div className={styles.apacheSourceLinks}>
          <a
            href="https://projects.apache.org/"
            target="_blank"
            rel="noreferrer"
            tabIndex={stage ? -1 : undefined}
          >
            Projects Directory <ArrowUpRightIcon aria-hidden="true" />
          </a>
          <a
            href="https://github.com/apache"
            target="_blank"
            rel="noreferrer"
            tabIndex={stage ? -1 : undefined}
          >
            GitHub apache org <ArrowUpRightIcon aria-hidden="true" />
          </a>
        </div>
      </div>
    </div>
  );
}
